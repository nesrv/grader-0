from fastapi import FastAPI

from app.api_v1.routes import router as api_v1_router
from app.init_db import init_db

# Инициализация базы данных
init_db()

app = FastAPI()

# Подключаем маршруты API v1
app.include_router(api_v1_router)

@app.get("/")
async def root():
    return {"message": "Простое FastAPI приложение с OAuth2 и JWT"}