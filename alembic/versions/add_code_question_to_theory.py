"""add_code_question_to_theory

Revision ID: add_code_question_to_theory
Revises: add_learning_materials
Create Date: 2023-05-20 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_code_question_to_theory'
down_revision = 'add_learning_materials'
branch_labels = None
depends_on = None


def upgrade():
    # Добавляем колонку code_question в таблицу theory
    op.add_column('theory', sa.Column('code_question', sa.Text(), nullable=True))
    
    # Обновляем существующие записи, устанавливая значение по умолчанию
    op.execute("UPDATE theory SET code_question = '' WHERE code_question IS NULL")
    
    # Делаем колонку не nullable после обновления данных
    op.alter_column('theory', 'code_question', nullable=False)


def downgrade():
    # Удаляем колонку code_question из таблицы theory
    op.drop_column('theory', 'code_question')