# Простое FastAPI приложение с OAuth2 + JWT

Минимальное приложение FastAPI с аутентификацией OAuth2 и JWT токенами.

## Установка

```bash
# Создание виртуального окружения
python3 -m venv venv
# Активация виртуального окружения
source venv/bin/activate  # для Linux/Mac
# или
# venv\Scripts\activate  # для Windows

# Установка зависимостей
pip install -r requirements.txt
```

## Запуск приложения

```bash
# Убедитесь, что виртуальное окружение активировано
source venv/bin/activate  # для Linux/Mac
# или
# venv\Scripts\activate  # для Windows

# Запуск сервера
uvicorn main:app --reload
```

## Структура проекта

```
.
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── init_db.py
│   └── api_v1/
│       ├── __init__.py
│       ├── routes.py
│       └── auth/
│           ├── __init__.py
│           ├── handlers.py
│           └── models.py
├── main.py
├── README.md
├── requirements.txt
└── grader.sqlite
```

## Использование

1. Запустите приложение
2. Откройте Swagger UI по адресу http://localhost:8000/docs
3. Авторизуйтесь через эндпоинт `/api/v1/users/token` с данными:
   - Username: user
   - Password: secret
4. Используйте полученный токен для доступа к защищенным эндпоинтам

## API эндпоинты

- `GET /` - Главная страница (публичная)
- `POST /api/v1/users/token` - Получение JWT токена
- `GET /api/v1/users/me` - Информация о текущем пользователе (защищенный эндпоинт)
- `PUT /api/v1/users/me` - Обновление данных текущего пользователя (защищенный эндпоинт)
- `GET /api/v1/users` - Получение списка всех пользователей (защищенный эндпоинт)
- `POST /api/v1/users` - Создание нового пользователя (публичный эндпоинт)
- `GET /api/v1/users/{user_id}` - Получение информации о пользователе по ID (защищенный эндпоинт)

создай api/v1/profession c файлами handlers, models, schemas, service

создай таблицу  в бд users.sqlite для этого app 

```py
class Profession(Base):
    __tablename__ = "professions"
    profession_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    image_path = Column(String, nullable=True)
```

добавь CRUD эндпоинты для работы с профессией


создай api/v1/graders c файлами handlers, models, schemas, service

```py
class Grades(Base):
    __tablename__ = "grades"
    grade_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    level = Column(Enum(GradeLevel), nullable=False, default=GradeLevel.JUNIOR)
    description = Column(Text, nullable=True)
    requirements = Column(Text, nullable=True)
    
    # Relations
    profession_id = Column(Integer, ForeignKey("profession.id"), nullable=False)
    profession = relationship("Profession", back_populates="grades")
    
```