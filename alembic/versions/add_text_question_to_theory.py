"""add_text_question_to_theory

Revision ID: add_text_question_to_theory
Revises: remove_answer_type_from_theory
Create Date: 2023-05-21 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'add_text_question_to_theory'
down_revision = 'remove_answer_type_from_theory'
branch_labels = None
depends_on = None


def upgrade():
    # SQLite не поддерживает ALTER COLUMN напрямую, поэтому используем обходной путь
    # 1. Создаем временную таблицу с новыми колонками
    op.execute('''
        CREATE TABLE theory_new (
            theory_id INTEGER NOT NULL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            code_question TEXT,
            text_question JSON,
            answer INTEGER,
            is_active BOOLEAN DEFAULT 1,
            topic_id INTEGER NOT NULL,
            FOREIGN KEY(topic_id) REFERENCES topics (topic_id)
        )
    ''')
    
    # 2. Копируем данные из старой таблицы в новую
    op.execute('''
        INSERT INTO theory_new (theory_id, title, description, code_question, is_active, topic_id)
        SELECT theory_id, title, description, code_question, is_active, topic_id FROM theory
    ''')
    
    # 3. Удаляем старую таблицу
    op.execute('DROP TABLE theory')
    
    # 4. Переименовываем новую таблицу
    op.execute('ALTER TABLE theory_new RENAME TO theory')
    
    # 5. Создаем индекс, если он был в оригинальной таблице
    op.execute('CREATE INDEX ix_theory_theory_id ON theory (theory_id)')


def downgrade():
    # Возвращаемся к предыдущей структуре таблицы
    op.execute('''
        CREATE TABLE theory_old (
            theory_id INTEGER NOT NULL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            code_question TEXT,
            is_active BOOLEAN DEFAULT 1,
            topic_id INTEGER NOT NULL,
            FOREIGN KEY(topic_id) REFERENCES topics (topic_id)
        )
    ''')
    
    op.execute('''
        INSERT INTO theory_old (theory_id, title, description, code_question, is_active, topic_id)
        SELECT theory_id, title, description, code_question, is_active, topic_id FROM theory
    ''')
    
    op.execute('DROP TABLE theory')
    op.execute('ALTER TABLE theory_old RENAME TO theory')
    op.execute('CREATE INDEX ix_theory_theory_id ON theory (theory_id)')