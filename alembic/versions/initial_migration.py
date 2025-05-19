"""initial_migration

Revision ID: initial_migration
Revises: 
Create Date: 2023-05-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Создание таблицы theory
    op.create_table('theory',
        sa.Column('theory_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('answer_type', sa.Enum('understand', 'not_understand', name='answer_type_enum'), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('topic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.topic_id'], ),
        sa.PrimaryKeyConstraint('theory_id')
    )
    op.create_index(op.f('ix_theory_theory_id'), 'theory', ['theory_id'], unique=False)

    # Создание таблицы questions
    op.create_table('questions',
        sa.Column('question_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('options', sqlite.JSON(), nullable=False),
        sa.Column('correct_answers', sqlite.JSON(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('topic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.topic_id'], ),
        sa.PrimaryKeyConstraint('question_id')
    )
    op.create_index(op.f('ix_questions_question_id'), 'questions', ['question_id'], unique=False)

    # Создание таблицы tasks
    op.create_table('tasks',
        sa.Column('task_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('code_question', sa.Text(), nullable=False),
        sa.Column('correct_answer', sa.Text(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('topic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.topic_id'], ),
        sa.PrimaryKeyConstraint('task_id')
    )
    op.create_index(op.f('ix_tasks_task_id'), 'tasks', ['task_id'], unique=False)

    # Создание таблицы cases
    op.create_table('cases',
        sa.Column('case_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('code_template', sa.Text(), nullable=False),
        sa.Column('correct_fields', sqlite.JSON(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('topic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.topic_id'], ),
        sa.PrimaryKeyConstraint('case_id')
    )
    op.create_index(op.f('ix_cases_case_id'), 'cases', ['case_id'], unique=False)


def downgrade():
    # Удаление таблиц в обратном порядке
    op.drop_index(op.f('ix_cases_case_id'), table_name='cases')
    op.drop_table('cases')
    op.drop_index(op.f('ix_tasks_task_id'), table_name='tasks')
    op.drop_table('tasks')
    op.drop_index(op.f('ix_questions_question_id'), table_name='questions')
    op.drop_table('questions')
    op.drop_index(op.f('ix_theory_theory_id'), table_name='theory')
    op.drop_table('theory')