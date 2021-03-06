"""empty message

Revision ID: cdc8c337782a
Revises: 6704c6bc1e48
Create Date: 2018-10-19 11:04:16.317804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cdc8c337782a'
down_revision = '6704c6bc1e48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reqbarang', sa.Column('is_done', sa.Boolean(), nullable=True))
    op.drop_column('reqbarang', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reqbarang', sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('reqbarang', 'is_done')
    # ### end Alembic commands ###
