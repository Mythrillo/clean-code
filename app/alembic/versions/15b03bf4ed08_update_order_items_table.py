"""Update order_items table

Revision ID: 15b03bf4ed08
Revises: 7d28e6a27613
Create Date: 2023-01-16 17:47:57.875816

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "15b03bf4ed08"
down_revision = "7d28e6a27613"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("order_items", sa.Column("amount", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_items", "amount")
    # ### end Alembic commands ###
