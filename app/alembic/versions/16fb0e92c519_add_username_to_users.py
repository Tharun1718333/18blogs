"""add username to users

Revision ID: 16fb0e92c519
Revises: 53084b44486c
Create Date: 2026-08-13 17:44:40.382194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16fb0e92c519'
down_revision: Union[str, Sequence[str], None] = '53084b44486c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = [column['name'] for column in inspector.get_columns('users')]
    if 'username' not in columns:
        op.add_column('users', sa.Column('username', sa.String(length=255), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    columns = [column['name'] for column in inspector.get_columns('users')]
    if 'username' in columns:
        op.drop_column('users', 'username')
