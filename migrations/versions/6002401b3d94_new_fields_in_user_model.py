"""new fields in user model

Revision ID: 6002401b3d94
Revises: 4410f71e5f4b
Create Date: 2022-08-21 10:16:25.140992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6002401b3d94'
down_revision = '4410f71e5f4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###