# -*- coding: utf-8 -*-
import json

from troika.database import Model, SurrogatePK, db
from troika.helpers import date_helper


class Card(SurrogatePK, Model):

    __tablename__ = 'cards'

    PER_PAGE = 50

    STATUS_NEW = 'new'
    STATUS_INPROGRESS = 'inprogress'
    STATUS_RELEASED = 'released'
    STATUS_DELIVERED = 'delivered'
    STATUS_REMOVED = 'removed'

    STATUS_TITLE = {STATUS_NEW: u'Новая',
                    STATUS_INPROGRESS: u'В процессе',
                    STATUS_RELEASED: u'Выпущена',
                    STATUS_DELIVERED: u'Доставлена',
                    STATUS_REMOVED: u'Удалена'}

    STATE_ACTIVE = 0
    STATE_LOST = 1
    STATE_BROKEN = 3
    STATE_NOT_NEED = 5
    STATE_REISSUED = 6

    TROIKA_STATE_TITLE = {STATE_ACTIVE: u'Рабочая',
                          STATE_LOST: u'Утеряна',
                          STATE_BROKEN: u'Испорчена',
                          STATE_NOT_NEED: u'Не нужна',
                          STATE_REISSUED: u'Перевыпущена'}

    hard_id = db.Column(db.String(128), unique=True, nullable=False)
    troika_id = db.Column(db.String(128), unique=True, nullable=False)
    name_ru = db.Column(db.String(300))
    name_en = db.Column(db.String(300))
    creation_date = db.Column(db.DateTime, nullable=False)
    troika_state = db.Column(db.Integer(), nullable=False, default=STATE_ACTIVE)
    status = db.Column(db.String(128), nullable=False, default=STATUS_NEW)

    def __init__(self, hard_id=None, troika_id=None, **kwargs):
        if hard_id and troika_id:
            self.hard_id = hard_id
            self.troika_id = troika_id
            self.creation_date = date_helper.get_current_date()
            self.troika_state = self.STATE_ACTIVE
            self.status = self.STATUS_NEW

        db.Model.__init__(self, **kwargs)

    def to_dict(self):
        return {
            'id': self.id,
            'hard_id': self.hard_id,
            'troika_id': self.troika_id,
            'name_ru': self.name_ru,
            'troika_state': self.troika_state,
            'status': self.status,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return '<Card ({hard_id!r})>'.format(hard_id=self.hard_id)
