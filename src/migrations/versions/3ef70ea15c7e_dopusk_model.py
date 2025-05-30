"""dopusk model

Revision ID: 3ef70ea15c7e
Revises: 3a13e2f660fd
Create Date: 2025-05-27 13:00:27.100754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = '3ef70ea15c7e'
down_revision: Union[str, None] = '3a13e2f660fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dopuski',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', ENUM('MODULE1', 'MODULE2', 'ZACHET', 'EXAM', name='gradeenum', create_type=False), server_default='MODULE1', nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('discipline_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['professor_id'], ['professors.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dopuski_id'), 'dopuski', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dopuski_id'), table_name='dopuski')
    op.drop_table('dopuski')
    # ### end Alembic commands ###
