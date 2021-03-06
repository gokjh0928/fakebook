"""added image attribute to User model

Revision ID: 46bc0483a00c
Revises: 82cc849a5f05
Create Date: 2021-07-09 10:56:52.422621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46bc0483a00c'
down_revision = '82cc849a5f05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image')
    # ### end Alembic commands ###
