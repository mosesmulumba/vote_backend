"""added index on password(unique=True)

Revision ID: 77280215301f
Revises: 3a4984f941b7
Create Date: 2024-06-20 20:28:11.054753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77280215301f'
down_revision = '3a4984f941b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('election', schema=None) as batch_op:
        batch_op.drop_index('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('election', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=True)

    # ### end Alembic commands ###