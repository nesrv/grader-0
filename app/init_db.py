from sqlalchemy.orm import Session

from app.database import SessionLocal, UserDB, Profession, Grade, GradeLevel, Module, Topic
from app.init_modules_data import init_modules_data

# Фейковые данные пользователей
fake_users_db = {
    "user": {
        "username": "user",
        "full_name": "John Doe",
        "email": "john@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # password: secret
        "disabled": False,
    }
}

# Данные профессий
professions_data = [
    {
        "name": "Бэкендер / Веб-разработчик",
        "description": "Разработка серверной части приложений с использованием фреймворков Django, Flask, FastAPI",
        "image_path": "/images/backend_developer.jpg"
    },
    {
        "name": "Аналитик данных / Data Scientist",
        "description": "Обработка и анализ данных с помощью библиотек Pandas, NumPy, Matplotlib",
        "image_path": "/images/data_scientist.jpg"
    },
    {
        "name": "AI-разработчик / ML Engineer",
        "description": "Построение моделей машинного обучения (Scikit-learn, PyTorch, TensorFlow, Keras)",
        "image_path": "/images/ml_engineer.jpg"
    },
    {
        "name": "DevOps-инженер / Инженер автоматизации",
        "description": "Автоматизация CI/CD Ansible, Docker, Kubernetes",
        "image_path": "/images/devops_engineer.jpg"
    },
    {
        "name": "QA Automation Engineer / Автоматизатор тестирования",
        "description": "Написание автотестов с помощью Selenium, PyTest",
        "image_path": "/images/qa_automation.jpg"
    },
    {
        "name": "Game Dev / Разработчик игр",
        "description": "Создание 2D-игр на Pygame, Kivy, разработка прототипов и инструментов для геймдева",
        "image_path": "/images/game_dev.jpg"
    },
    {
        "name": "Разработчик IoT / Системный программист",
        "description": "Программирование микроконтроллеров Raspberry Pi, Arduino. Автоматизация умных устройств",
        "image_path": "/images/iot_developer.jpg"
    }
]

# Данные грейдов
grades_data = [
    # 1. Бэкендер / Веб-разработчик
    {"level_name": GradeLevel.STAGER, "description": "Основы языка, базовые структуры данных, простые скрипты, понимание HTTP и REST.", "profession_id": 1},
    {"level_name": GradeLevel.JUNIOR, "description": "ООП, работа с базами данных (SQL/NoSQL), основы веб-фреймворков (FastAPI/Django), написание API, работа с Git.", "profession_id": 1},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Уверенное владение фреймворками, REST/JSON, обработка ошибок, базовое тестирование, документация, работа с внешними API.", "profession_id": 1},
    {"level_name": GradeLevel.MIDDLE, "description": "Проектирование архитектуры, слоистая структура приложений, профилирование и оптимизация, кеширование, безопасность, CI/CD.", "profession_id": 1},
    {"level_name": GradeLevel.SENIOR, "description": "Системный дизайн, техническое лидерство, код-ревью, менторство, управление архитектурой проекта, участие в найме и развитии команды.", "profession_id": 1},
    
    # 2. Аналитик данных / Data Scientist
    {"level_name": GradeLevel.STAGER, "description": "Базовый Python, pandas, matplotlib, основы статистики, SQL, понимание задач анализа данных.", "profession_id": 2},
    {"level_name": GradeLevel.JUNIOR, "description": "Уверенное владение pandas/numpy, визуализация (seaborn, plotly), SQL-запросы, базовые ML-модели (sklearn), понимание бизнес-целей.", "profession_id": 2},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Самостоятельная работа с датасетами, построение и оценка моделей, feature engineering, основы A/B тестов, регуляризация, основы ML pipeline.", "profession_id": 2},
    {"level_name": GradeLevel.MIDDLE, "description": "Продвинутый sklearn, ML pipeline, продвинутая визуализация, продвинутый SQL, статистическая проверка гипотез, участие в продакшн-проектах, понимание метрик качества.", "profession_id": 2},
    {"level_name": GradeLevel.SENIOR, "description": "Лидерство в проектах, проектирование ML-архитектуры, оптимизация бизнес-метрик через модели, внедрение моделей в продакшн, знание MLOps, системное мышление, наставничество.", "profession_id": 2},
    
    # 3. AI-разработчик / ML Engineer
    {"level_name": GradeLevel.STAGER, "description": "Основы Python, numpy/pandas, базовая линейная алгебра и статистика, понимание принципов машинного обучения, sklearn.", "profession_id": 3},
    {"level_name": GradeLevel.JUNIOR, "description": "Классические ML-модели (sklearn), подготовка данных, метрики качества, простые пайплайны, работа с готовыми датасетами, базовая визуализация.", "profession_id": 3},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Глубокое понимание моделей, гиперпараметры, feature engineering, кросс-валидация, начало работы с нейросетями (PyTorch/TensorFlow), участие в продакшн-разработке.", "profession_id": 3},
    {"level_name": GradeLevel.MIDDLE, "description": "Построение ML-систем end-to-end, эксперименты и сравнение моделей, кастомные пайплайны, MLOps основы (DVC, MLflow), API-сервинг, работа с данными из продакшна.", "profession_id": 3},
    {"level_name": GradeLevel.SENIOR, "description": "Стратегическое планирование ML-продуктов, интеграция ML в бизнес, системный дизайн, лидерство в ML-командах, исследование новых подходов, публикации/прототипирование, менторство.", "profession_id": 3},
    
    # 4. DevOps-инженер / Инженер автоматизации
    {"level_name": GradeLevel.STAGER, "description": "Основы Linux, базовые команды bash, понимание сетей, установка ПО, работа с Git, базовые знания CI/CD.", "profession_id": 4},
    {"level_name": GradeLevel.JUNIOR, "description": "Написание bash-скриптов, настройка простых пайплайнов (GitLab CI, GitHub Actions), базовая работа с Docker, начальное понимание мониторинга и логирования.", "profession_id": 4},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Уверенная работа с Docker, настройка CI/CD-процессов, автоматизация деплоя, понимание Kubernetes, базовая работа с облаками (AWS/GCP), работа с Ansible/Terraform.", "profession_id": 4},
    {"level_name": GradeLevel.MIDDLE, "description": "Инфраструктура как код (IaC), CI/CD для микросервисов, настройка и масштабирование кластеров Kubernetes, мониторинг (Prometheus, Grafana), логирование (ELK, Loki), безопасность (secrets, IAM, TLS).", "profession_id": 4},
    {"level_name": GradeLevel.SENIOR, "description": "Проектирование архитектуры инфраструктуры, SLA/SLO стратегии, оптимизация стоимости облака, техническое лидерство, внедрение процессов SRE/DevOps, менторство, участие в архитектурных решениях всей компании.", "profession_id": 4},
    
    # 5. QA Automation Engineer / Автоматизатор тестирования
    {"level_name": GradeLevel.STAGER, "description": "Основы Python, понимание процессов тестирования, базовые знания HTML/CSS/JS, написание простых тестов.", "profession_id": 5},
    {"level_name": GradeLevel.JUNIOR, "description": "Написание автотестов с использованием PyTest, базовая работа с Selenium, понимание CI/CD для тестов, работа с API.", "profession_id": 5},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Разработка фреймворков для тестирования, работа с Page Object Model, интеграция тестов в CI/CD, параллельное выполнение тестов.", "profession_id": 5},
    {"level_name": GradeLevel.MIDDLE, "description": "Комплексные стратегии тестирования, нагрузочное тестирование, мок-сервисы, автоматизация отчетности, интеграция с системами управления тестированием.", "profession_id": 5},
    {"level_name": GradeLevel.SENIOR, "description": "Архитектура тестовых фреймворков, стратегии обеспечения качества, управление тестовыми данными, менторство, участие в планировании разработки с учетом тестирования.", "profession_id": 5},
    
    # 6. Game Dev / Разработчик игр
    {"level_name": GradeLevel.STAGER, "description": "Основы Python, базовые алгоритмы, работа с Pygame, понимание игрового цикла, простая графика и управление.", "profession_id": 6},
    {"level_name": GradeLevel.JUNIOR, "description": "Разработка простых 2D-игр, работа с спрайтами и анимацией, обработка столкновений, базовая физика, звуковые эффекты.", "profession_id": 6},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Создание игровых механик, работа с Kivy/PyGame, оптимизация производительности, интеграция с внешними библиотеками, создание прототипов.", "profession_id": 6},
    {"level_name": GradeLevel.MIDDLE, "description": "Архитектура игровых движков, продвинутая физика, AI для игр, многопользовательские игры, интеграция с базами данных, кроссплатформенная разработка.", "profession_id": 6},
    {"level_name": GradeLevel.SENIOR, "description": "Разработка игровых движков, оптимизация производительности, руководство командой разработки, интеграция с 3D-движками, создание инструментов для геймдева.", "profession_id": 6},
    
    # 7. Разработчик IoT / Системный программист
    {"level_name": GradeLevel.STAGER, "description": "Основы Python, работа с GPIO, базовые электронные компоненты, простые скрипты для Raspberry Pi/Arduino.", "profession_id": 7},
    {"level_name": GradeLevel.JUNIOR, "description": "Работа с датчиками и актуаторами, протоколы связи (I2C, SPI), базовые сетевые протоколы, простые IoT-проекты.", "profession_id": 7},
    {"level_name": GradeLevel.JUNIOR_PLUS, "description": "Разработка IoT-систем, работа с MQTT/CoAP, интеграция с облачными платформами, обработка данных с датчиков в реальном времени.", "profession_id": 7},
    {"level_name": GradeLevel.MIDDLE, "description": "Архитектура IoT-систем, безопасность IoT, оптимизация энергопотребления, работа с низкоуровневыми интерфейсами, распределенные системы.", "profession_id": 7},
    {"level_name": GradeLevel.SENIOR, "description": "Проектирование сложных IoT-экосистем, интеграция с ML/AI, разработка протоколов и стандартов, оптимизация производительности, руководство IoT-проектами.", "profession_id": 7}
]

def init_db():
    db = SessionLocal()
    
    # Проверяем, есть ли уже пользователи в базе
    user_count = db.query(UserDB).count()
    if user_count == 0:
        # Добавляем тестового пользователя
        for username, user_data in fake_users_db.items():
            db_user = UserDB(
                username=user_data["username"],
                email=user_data["email"],
                full_name=user_data["full_name"],
                hashed_password=user_data["hashed_password"],
                disabled=user_data["disabled"]
            )
            db.add(db_user)
    
    # Удаляем все существующие профессии
    db.query(Profession).delete()
    
    # Добавляем профессии
    for profession_data in professions_data:
        db_profession = Profession(**profession_data)
        db.add(db_profession)
    
    db.commit()
    
    # Удаляем все существующие грейды
    db.query(Grade).delete()
    
    # Добавляем грейды
    for grade_data in grades_data:
        db_grade = Grade(**grade_data)
        db.add(db_grade)
    
    db.commit()
    
    # Удаляем все существующие модули и темы
    db.query(Topic).delete()
    db.query(Module).delete()
    
    # Инициализируем модули и темы
    init_modules_data(db)
    
    db.close()

if __name__ == "__main__":
    init_db()
    print("База данных инициализирована.")