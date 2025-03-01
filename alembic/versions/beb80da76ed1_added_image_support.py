"""Added image support

Revision ID: beb80da76ed1
Revises: c611033e3a1c
Create Date: 2022-06-06 00:01:01.499421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beb80da76ed1'
down_revision = 'c611033e3a1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.VARCHAR(length=100), nullable=True),
    sa.Column('name', sa.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    # ### end Alembic commands ###
