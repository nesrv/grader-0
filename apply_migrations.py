import sqlite3
import os

def apply_migrations():
    """Применяет миграции напрямую через SQL"""
    
    # Проверяем существование базы данных
    db_path = "grader.sqlite"
    if not os.path.exists(db_path):
        print(f"База данных {db_path} не найдена")
        return
    
    # Подключаемся к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Проверяем существование таблицы theory
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='theory'")
        if not cursor.fetchone():
            print("Создаю таблицу theory...")
            cursor.execute('''
            CREATE TABLE theory (
                theory_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                answer_type VARCHAR(20) NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                topic_id INTEGER NOT NULL,
                FOREIGN KEY (topic_id) REFERENCES topics (topic_id)
            )
            ''')
            cursor.execute('CREATE INDEX ix_theory_theory_id ON theory (theory_id)')
        
        # Проверяем существование таблицы questions
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")
        if not cursor.fetchone():
            print("Создаю таблицу questions...")
            cursor.execute('''
            CREATE TABLE questions (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                options TEXT NOT NULL,
                correct_answers TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                topic_id INTEGER NOT NULL,
                FOREIGN KEY (topic_id) REFERENCES topics (topic_id)
            )
            ''')
            cursor.execute('CREATE INDEX ix_questions_question_id ON questions (question_id)')
        
        # Проверяем существование таблицы tasks
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
        if not cursor.fetchone():
            print("Создаю таблицу tasks...")
            cursor.execute('''
            CREATE TABLE tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                code_question TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                topic_id INTEGER NOT NULL,
                FOREIGN KEY (topic_id) REFERENCES topics (topic_id)
            )
            ''')
            cursor.execute('CREATE INDEX ix_tasks_task_id ON tasks (task_id)')
        
        # Проверяем существование таблицы cases
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cases'")
        if not cursor.fetchone():
            print("Создаю таблицу cases...")
            cursor.execute('''
            CREATE TABLE cases (
                case_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                code_template TEXT NOT NULL,
                correct_fields TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                topic_id INTEGER NOT NULL,
                FOREIGN KEY (topic_id) REFERENCES topics (topic_id)
            )
            ''')
            cursor.execute('CREATE INDEX ix_cases_case_id ON cases (case_id)')
        
        # Сохраняем изменения
        conn.commit()
        print("Миграции успешно применены")
    
    except Exception as e:
        conn.rollback()
        print(f"Ошибка при применении миграций: {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    apply_migrations()