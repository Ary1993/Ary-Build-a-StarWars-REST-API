"""empty message

Revision ID: 955117a70d3d
Revises: c4f07dc032a8
Create Date: 2024-02-29 19:00:32.013324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955117a70d3d'
down_revision = 'c4f07dc032a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planets_id'),
    sa.UniqueConstraint('user_id')
    )
    op.drop_table('favorite__planets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite__planets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planets_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], name='favorite__planets_planets_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='favorite__planets_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorite__planets_pkey'),
    sa.UniqueConstraint('planets_id', name='favorite__planets_planets_id_key'),
    sa.UniqueConstraint('user_id', name='favorite__planets_user_id_key')
    )
    op.drop_table('favorite_planets')
    # ### end Alembic commands ###
