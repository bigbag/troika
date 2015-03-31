"""empty message

Revision ID: 43aaabba1c7e
Revises: 2ecc61d2ebc4
Create Date: 2015-03-29 16:00:56.606979

"""

# revision identifiers, used by Alembic.
revision = '43aaabba1c7e'
down_revision = '2ecc61d2ebc4'

import sqlalchemy as sa
from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cards',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('hard_id', sa.String(length=128), nullable=False),
                    sa.Column('troika_id', sa.String(length=128), nullable=False),
                    sa.Column('name_ru', sa.String(length=300), nullable=True),
                    sa.Column('name_en', sa.String(length=300), nullable=True),
                    sa.Column('creation_date', sa.DateTime(), nullable=False),
                    sa.Column('troika_state', sa.Integer(), nullable=False, server_default='0'),
                    sa.Column('status', sa.String(length=128), nullable=False, server_default='new'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('hard_id'),
                    sa.UniqueConstraint('troika_id')
                    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cards')
    ### end Alembic commands ###
