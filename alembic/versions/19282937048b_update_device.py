"""update device

Revision ID: 19282937048b
Revises: c01ca46701f2
Create Date: 2023-05-31 17:07:43.940443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '19282937048b'
down_revision = 'c01ca46701f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'address')
    op.drop_column('users', 'config')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('config', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
