from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api_v1.routes import router as api_v1_router
from app.init_db import init_db

# Инициализация базы данных
init_db()

# Настройка CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "*"
]

app = FastAPI()

# Добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты API v1
app.include_router(api_v1_router)

@app.get("/")
async def root():
    return {"message": "Простое FastAPI приложение с OAuth2 и JWT"}