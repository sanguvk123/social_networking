"""followers

Revision ID: e81483b7af76
Revises: 0e23aefd9440
Create Date: 2020-02-21 11:13:22.375867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e81483b7af76'
down_revision = '0e23aefd9440'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('likes',
    sa.Column('liker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['liker_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    op.drop_table('followers')
    # ### end Alembic commands ###
