# -*- coding: utf-8 -*-
import logging
from troika.app import create_app

try:
    from troika.settings_local import Config
except Exception as e:
    logging.exception("Exception: %(body)s", {'body': e})
    from troika.settings import Config

app = create_app(Config)
