"""Initial migration.

Revision ID: dee9e5d7a8cc
Revises: 
Create Date: 2020-07-15 21:46:29.758209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dee9e5d7a8cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('speakers')
    op.drop_table('events')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('events_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('subject', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('event_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='events_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('speakers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('expertise', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='speakers_event_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='speakers_pkey')
    )
    # ### end Alembic commands ###
