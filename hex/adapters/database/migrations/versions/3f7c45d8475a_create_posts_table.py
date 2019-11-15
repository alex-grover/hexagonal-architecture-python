"""create posts table

Revision ID: 3f7c45d8475a
Revises:
Create Date: 2019-11-08 20:43:11.106250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f7c45d8475a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('author_name', sa.Text, nullable=False),
        sa.Column('title', sa.Text, nullable=False),
        sa.Column('body', sa.Text, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now(),
                  onupdate=sa.func.now()),
    )


def downgrade():
    op.drop_table('posts')
