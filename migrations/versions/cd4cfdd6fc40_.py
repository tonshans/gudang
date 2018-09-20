"""empty message

Revision ID: cd4cfdd6fc40
Revises: e6cf8310fb04
Create Date: 2018-09-18 14:18:31.929201

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cd4cfdd6fc40'
down_revision = 'e6cf8310fb04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('inventory_ibfk_1', 'inventory', type_='foreignkey')
    op.drop_constraint('inventory_ibfk_3', 'inventory', type_='foreignkey')
    op.drop_column('inventory', 'asal')
    op.drop_column('inventory', 'tujuan')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory', sa.Column('tujuan', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('inventory', sa.Column('asal', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('inventory_ibfk_3', 'inventory', 'alamat', ['tujuan'], ['id'])
    op.create_foreign_key('inventory_ibfk_1', 'inventory', 'alamat', ['asal'], ['id'])
    # ### end Alembic commands ###