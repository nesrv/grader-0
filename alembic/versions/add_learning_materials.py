\"\"\"add_learning_materials

Revision ID: add_learning_materials
Revises: initial_migration
Create Date: 2023-05-19 00:00:00.000000

\"\"\"
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'add_learning_materials'
down_revision = 'initial_migration'
branch_labels = None
depends_on = None


def upgrade():
    # Эта миграция не создает новые таблицы, так как они уже существуют
    # Здесь можно добавить изменения в существующие таблицы, если необходимо
    pass


def downgrade():
    # Так как мы не делаем изменений в upgrade(), здесь тоже ничего не делаем
    pass