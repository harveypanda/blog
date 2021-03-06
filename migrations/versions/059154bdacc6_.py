"""empty message

Revision ID: 059154bdacc6
Revises: bc935e39285d
Create Date: 2019-01-26 14:47:38.071231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '059154bdacc6'
down_revision = 'bc935e39285d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('isRecommand', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'isRecommand')
    # ### end Alembic commands ###
