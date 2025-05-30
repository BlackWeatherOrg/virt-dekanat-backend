"""grades deleted issued date

Revision ID: 7f8e9cf59f4a
Revises: 6d95bd687aae
Create Date: 2025-05-25 21:31:52.203700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f8e9cf59f4a'
down_revision: Union[str, None] = '6d95bd687aae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grades', 'issued_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grades', sa.Column('issued_date', sa.DATE(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
