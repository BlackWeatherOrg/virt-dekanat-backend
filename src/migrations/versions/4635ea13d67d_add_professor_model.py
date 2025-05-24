"""Add Professor Model

Revision ID: 4635ea13d67d
Revises: 8cb708288715
Create Date: 2025-05-24 23:01:50.026465

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4635ea13d67d'
down_revision: Union[str, None] = '8cb708288715'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
