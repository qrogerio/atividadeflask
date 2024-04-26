"""empty message

Revision ID: 2088f0bab561
Revises: 
Create Date: 2024-04-26 20:39:23.388338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2088f0bab561'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unidadecompetencia',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.Column('carga_horaria', sa.Integer(), nullable=True),
    sa.Column('competencia_geral', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('unidadecompetencia')
    # ### end Alembic commands ###
