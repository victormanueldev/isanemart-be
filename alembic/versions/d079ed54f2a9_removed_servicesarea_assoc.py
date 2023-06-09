"""Removed servicesarea assoc

Revision ID: d079ed54f2a9
Revises: d137afbfea5a
Create Date: 2023-05-17 09:31:33.447558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd079ed54f2a9'
down_revision = 'd137afbfea5a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('servicearea')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('servicearea',
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('area_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['area.id'], name='servicearea_area_id_fkey'),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], name='servicearea_service_id_fkey'),
    sa.PrimaryKeyConstraint('service_id', 'area_id', name='servicearea_pkey')
    )
    # ### end Alembic commands ###
