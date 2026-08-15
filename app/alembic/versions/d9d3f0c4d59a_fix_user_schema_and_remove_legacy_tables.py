"""fix user schema and remove legacy tables

Revision ID: d9d3f0c4d59a
Revises: c3f4e85c8e1b
Create Date: 2026-08-13 21:45:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd9d3f0c4d59a'
down_revision: Union[str, Sequence[str], None] = 'c3f4e85c8e1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()

    def get_user_columns():
        return [column['name'] for column in sa.inspect(bind).get_columns('users')]

    user_columns = get_user_columns()
    if 'gmail' not in user_columns and 'email' in user_columns:
        op.alter_column('users', 'email', new_column_name='gmail')

    user_columns = get_user_columns()
    if 'created_on' not in user_columns:
        op.add_column(
            'users',
            sa.Column('created_on', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        )

    user_columns = get_user_columns()
    if 'updated_on' not in user_columns:
        op.add_column(
            'users',
            sa.Column('updated_on', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        )

    user_columns = get_user_columns()
    if 'name' in user_columns:
        op.drop_column('users', 'name')

    user_columns = get_user_columns()
    if 'email' in user_columns:
        op.drop_column('users', 'email')

    if 'notes' in sa.inspect(bind).get_table_names():
        op.drop_table('notes')


def downgrade() -> None:
    bind = op.get_bind()

    def get_user_columns():
        return [column['name'] for column in sa.inspect(bind).get_columns('users')]

    user_columns = get_user_columns()
    if 'gmail' in user_columns and 'email' not in user_columns:
        op.alter_column('users', 'gmail', new_column_name='email')

    user_columns = get_user_columns()
    if 'created_on' in user_columns:
        op.drop_column('users', 'created_on')

    user_columns = get_user_columns()
    if 'updated_on' in user_columns:
        op.drop_column('users', 'updated_on')

    user_columns = get_user_columns()
    if 'name' not in user_columns:
        op.add_column('users', sa.Column('name', sa.String(length=100), nullable=True))

    if 'notes' not in sa.inspect(bind).get_table_names():
        op.create_table(
            'notes',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('title', sa.String(length=200), nullable=False),
            sa.Column('content', sa.Text(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=True),
            sa.PrimaryKeyConstraint('id'),
        )
