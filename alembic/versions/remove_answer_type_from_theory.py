"""remove_answer_type_from_theory

Revision ID: remove_answer_type_from_theory
Revises: add_code_question_to_theory
Create Date: 2023-05-21 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'remove_answer_type_from_theory'
down_revision = 'add_code_question_to_theory'
branch_labels = None
depends_on = None


def upgrade():
    # SQLite не поддерживает DROP COLUMN напрямую, поэтому используем обходной путь
    # 1. Создаем временную таблицу без колонки answer_type
    op.execute('''
        CREATE TABLE theory_new (
            theory_id INTEGER NOT NULL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            code_question TEXT NOT NULL,
            is_active BOOLEAN,
            topic_id INTEGER NOT NULL,
            description TEXT,
            FOREIGN KEY(topic_id) REFERENCES topics (topic_id)
        )
    ''')
    
    # 2. Копируем данные из старой таблицы в новую
    op.execute('''
        INSERT INTO theory_new (theory_id, title, code_question, is_active, topic_id, description)
        SELECT theory_id, title, code_question, is_active, topic_id, description FROM theory
    ''')
    
    # 3. Удаляем старую таблицу
    op.execute('DROP TABLE theory')
    
    # 4. Переименовываем новую таблицу
    op.execute('ALTER TABLE theory_new RENAME TO theory')
    
    # 5. Создаем индекс, если он был в оригинальной таблице
    op.execute('CREATE INDEX ix_theory_theory_id ON theory (theory_id)')


def downgrade():
    # Восстанавливаем колонку answer_type (с значением по умолчанию 'understand')
    op.execute('''
        CREATE TABLE theory_old (
            theory_id INTEGER NOT NULL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            answer_type VARCHAR(14) NOT NULL,
            code_question TEXT NOT NULL,
            is_active BOOLEAN,
            topic_id INTEGER NOT NULL,
            description TEXT,
            FOREIGN KEY(topic_id) REFERENCES topics (topic_id)
        )
    ''')
    
    op.execute('''
        INSERT INTO theory_old (theory_id, title, answer_type, code_question, is_active, topic_id, description)
        SELECT theory_id, title, 'understand', code_question, is_active, topic_id, description FROM theory
    ''')
    
    op.execute('DROP TABLE theory')
    op.execute('ALTER TABLE theory_old RENAME TO theory')
    op.execute('CREATE INDEX ix_theory_theory_id ON theory (theory_id)')