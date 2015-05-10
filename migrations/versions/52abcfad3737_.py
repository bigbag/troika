"""empty message

Revision ID: 52abcfad3737
Revises: 4750b8ddc267
Create Date: 2015-05-10 15:42:53.569371

"""

# revision identifiers, used by Alembic.
revision = '52abcfad3737'
down_revision = '4750b8ddc267'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'orders', ['user_email'])
    op.create_unique_constraint(None, 'orders', ['user_id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='unique')
    op.drop_constraint(None, 'orders', type_='unique')
    ### end Alembic commands ###
