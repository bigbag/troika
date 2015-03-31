"""empty message

Revision ID: 2a983c0c392e
Revises: 1d9bd3b9c346
Create Date: 2015-03-30 23:06:57.372994

"""

# revision identifiers, used by Alembic.
revision = '2a983c0c392e'
down_revision = '1d9bd3b9c346'

import sqlalchemy as sa
from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cards_history', sa.Column('action', sa.String(length=128), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cards_history', 'action')
    ### end Alembic commands ###
