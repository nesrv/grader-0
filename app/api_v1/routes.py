from fastapi import APIRouter, Depends

from app.api_v1.auth.router import router as user_router
from app.api_v1.profession.router import router as profession_router
from app.api_v1.grade.router import router as grade_router
from app.api_v1.home.router import router as home_router
from app.api_v1.module.router import router as module_router
from app.api_v1.topic.router import router as topic_router
from app.api_v1.auth.handlers import get_current_active_user

# Создаем основной роутер для API v1
router = APIRouter(prefix="/api/v1")

# Подключаем роутер главной страницы
router.include_router(
    home_router,
    prefix="/home",
    tags=["Главная страница"],
)

# Подключаем роутер пользователей
router.include_router(
    user_router,
    prefix="/users",
    tags=["Пользователи"],
)

# Подключаем роутер профессий
router.include_router(
    profession_router,
    prefix="/professions",
    tags=["Специальности"],
)

# Подключаем роутер грейдов
router.include_router(
    grade_router,
    prefix="/grades",
    tags=["Грейды"],
)

# Подключаем роутер модулей
router.include_router(
    module_router,
    prefix="/modules",
    tags=["Модули"],
)

# Подключаем роутер тем и учебных материалов
router.include_router(
    topic_router,
    prefix="/topics",
    tags=["Темы и учебные материалы"],
)