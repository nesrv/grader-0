from sqlalchemy.orm import Session
from app.database import Grade, Module, Topic

def init_modules_data(db: Session):
    """
    Initialize modules and topics data.
    """
    # Check if data already exists
    if db.query(Module).count() > 0:
        print("Modules data already initialized")
        return
    
    # Get the intern grade for backend developer (assuming it exists)
    intern_grade = db.query(Grade).filter(
        Grade.level_name == "STAGER",  # Using the actual value stored in the database
        Grade.profession_id == 1  # Assuming 1 is the ID for backend developer
    ).first()
    
    if not intern_grade:
        print("Intern grade for backend developer not found")
        return
    
    # Create modules and topics
    modules_data = [
        {
            "title": "Основы Python",
            "description": "Базовые концепции языка Python",
            "order": 1,
            "topics": [
                {"title": "Простые неизменяемые типы данных", "order": 1},
                {"title": "Переменные и именование", "order": 2},
                {"title": "Ссылочная модель в Python, функция id(), оператор is", "order": 3},
                {"title": "Ввод/вывод данных", "order": 4},
                {"title": "Форматирование данных: %, str.format(), f-strings", "order": 5},
                {"title": "Арифметические и логические операции", "order": 6}
            ]
        },
        {
            "title": "Управляющие конструкции",
            "description": "Условные операторы и управление потоком выполнения",
            "order": 2,
            "topics": [
                {"title": "Условные операторы: if, elif, else", "order": 1},
                {"title": "Операторы сравнения", "order": 2},
                {"title": "Логические операторы: and, or, not", "order": 3},
                {"title": "Тернарный оператор", "order": 4},
                {"title": "Оператор match/case", "order": 5}
            ]
        },
        {
            "title": "Циклы и итерации",
            "description": "Работа с циклами и итерациями в Python",
            "order": 3,
            "topics": [
                {"title": "Циклы while и for", "order": 1},
                {"title": "Функция range()", "order": 2},
                {"title": "Управление циклами: break, continue, else", "order": 3},
                {"title": "enumerate() и zip()", "order": 4},
                {"title": "Вложенные циклы", "order": 5}
            ]
        },
        {
            "title": "Работа со строками",
            "description": "Манипуляции со строками и текстовыми данными",
            "order": 4,
            "topics": [
                {"title": "Индексы и срезы", "order": 1},
                {"title": "Основные методы строк", "order": 2},
                {"title": "Форматирование: f-строки", "order": 3},
                {"title": "Базовые регулярные выражения", "order": 4},
                {"title": "Кодировки и Unicode", "order": 5}
            ]
        },
        {
            "title": "Списки и генераторы",
            "description": "Работа со списками и генераторами списков",
            "order": 5,
            "topics": [
                {"title": "Создание и модификация списков", "order": 1},
                {"title": "Методы списков", "order": 2},
                {"title": "List comprehensions", "order": 3},
                {"title": "Срезы с шагом", "order": 4},
                {"title": "Вложенные списки", "order": 5}
            ]
        },
        {
            "title": "Словари и множества",
            "description": "Работа со словарями и множествами",
            "order": 6,
            "topics": [
                {"title": "Создание и работа со словарями", "order": 1},
                {"title": "Методы словарей", "order": 2},
                {"title": "Dictionary comprehensions", "order": 3},
                {"title": "Множества и операции над ними", "order": 4},
                {"title": "Генераторы множеств", "order": 5}
            ]
        },
        {
            "title": "Функции",
            "description": "Создание и использование функций",
            "order": 7,
            "topics": [
                {"title": "Создание и вызов функций", "order": 1},
                {"title": "Параметры и аргументы", "order": 2},
                {"title": "Возврат значений (return)", "order": 3},
                {"title": "Type hints (аннотации типов)", "order": 4},
                {"title": "Документирование функций (docstrings)", "order": 5},
                {"title": "Лямбда-функции", "order": 6}
            ]
        },
        {
            "title": "Модули и пакеты",
            "description": "Работа с модулями и пакетами Python",
            "order": 8,
            "topics": [
                {"title": "Импорт модулей", "order": 1},
                {"title": "Стандартные модули: math, random, sys", "order": 2},
                {"title": "Создание собственных модулей", "order": 3},
                {"title": "Установка пакетов (pip)", "order": 4},
                {"title": "Виртуальные окружения", "order": 5}
            ]
        },
        {
            "title": "Работа с файлами",
            "description": "Чтение и запись файлов",
            "order": 9,
            "topics": [
                {"title": "Открытие и закрытие файлов (with)", "order": 1},
                {"title": "Чтение и запись текстовых файлов", "order": 2},
                {"title": "Модуль pathlib для работы с путями", "order": 3},
                {"title": "CSV и JSON файлы", "order": 4}
            ]
        },
        {
            "title": "Обработка ошибок",
            "description": "Обработка исключений и ошибок",
            "order": 10,
            "topics": [
                {"title": "Конструкции try/except/finally", "order": 1},
                {"title": "Иерархия исключений", "order": 2},
                {"title": "Создание собственных исключений", "order": 3},
                {"title": "Оператор assert", "order": 4}
            ]
        },
        {
            "title": "Работа с данными",
            "description": "Работа с различными форматами данных",
            "order": 11,
            "topics": [
                {"title": "CSV файлы (модуль csv)", "order": 1},
                {"title": "JSON данные (модуль json)", "order": 2},
                {"title": "SQLite базы данных (sqlite3)", "order": 3},
                {"title": "Работа с Excel (openpyxl basics)", "order": 4}
            ]
        },
        {
            "title": "Дата и время",
            "description": "Работа с датами и временем",
            "order": 12,
            "topics": [
                {"title": "Модуль datetime", "order": 1},
                {"title": "Форматирование даты и времени", "order": 2},
                {"title": "Разница между датами (timedelta)", "order": 3},
                {"title": "Часовые пояса (базово)", "order": 4}
            ]
        }
    ]
    
    # Create modules and topics
    for module_data in modules_data:
        topics_data = module_data.pop("topics")
        
        module = Module(
            grade_id=intern_grade.grade_id,
            **module_data
        )
        db.add(module)
        db.flush()  # Flush to get the module_id
        
        # Create topics for this module
        for topic_data in topics_data:
            topic = Topic(
                module_id=module.module_id,
                **topic_data
            )
            db.add(topic)
    
    # Commit all changes
    db.commit()
    print("Modules and topics data initialized successfully")


