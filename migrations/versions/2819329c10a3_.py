"""empty message

Revision ID: 2819329c10a3
Revises: 2a25d388223
Create Date: 2015-04-24 18:42:16.096365

"""

# revision identifiers, used by Alembic.
revision = '2819329c10a3'
down_revision = '2a25d388223'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_cards_report_state'), 'cards', ['report_state'], unique=False)
    op.create_index(op.f('ix_cards_troika_state'), 'cards', ['troika_state'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cards_troika_state'), table_name='cards')
    op.drop_index(op.f('ix_cards_report_state'), table_name='cards')
    ### end Alembic commands ###
