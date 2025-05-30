"""changed professors to json

Revision ID: 25c20c27e097
Revises: 7f8e9cf59f4a
Create Date: 2025-05-27 02:03:36.013292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25c20c27e097'
down_revision: Union[str, None] = '7f8e9cf59f4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE disciplines SET authors = '[]'")

    op.alter_column('disciplines', 'authors',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.JSON(),
               postgresql_using='authors::json',
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE disciplines SET authors = ''")
    op.alter_column('disciplines', 'authors',
               existing_type=sa.JSON(),
               type_=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###
