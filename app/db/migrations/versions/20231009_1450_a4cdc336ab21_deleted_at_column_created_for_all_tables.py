"""deleted_at column created for all tables

Revision ID: a4cdc336ab21
Revises: e26be6b5e713
Create Date: 2023-10-09 14:50:10.574610

"""
import sqlalchemy as sa
from alembic import op
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "a4cdc336ab21"
down_revision: Union[str, None] = "e26be6b5e713"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("choices", sa.Column("deleted_at", sa.DateTime(), nullable=True))
    op.add_column("games", sa.Column("deleted_at", sa.DateTime(), nullable=True))
    op.add_column("scenes", sa.Column("deleted_at", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("scenes", "deleted_at")
    op.drop_column("games", "deleted_at")
    op.drop_column("choices", "deleted_at")
    # ### end Alembic commands ###