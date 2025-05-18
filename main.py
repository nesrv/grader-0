from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.api_v1.routes import router as api_v1_router
# from app.init_db import init_db

# Инициализация базы данных
# init_db()

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

# Монтируем статические файлы
app.mount("/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/js", StaticFiles(directory="frontend/js"), name="js")
app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")
app.mount("/images", StaticFiles(directory="frontend/assets/images"), name="images")
app.mount("/professions", StaticFiles(directory="frontend/assets/images/professions"), name="professions_images")

# Добавляем маршрут для profession.html
@app.get("/profession.html", response_class=HTMLResponse)
async def read_profession(request: Request):
    return templates.TemplateResponse("profession.html", {"request": request})

# Добавляем маршрут для grade.html
@app.get("/grade.html", response_class=HTMLResponse)
async def read_grade(request: Request):
    return templates.TemplateResponse("grade.html", {"request": request})

# Создаем шаблоны
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/learning", response_class=HTMLResponse)
async def read_learning(request: Request):
    return templates.TemplateResponse("learning.html", {"request": request})

@app.get("/learning.html", response_class=HTMLResponse)
async def read_learning_html(request: Request):
    return templates.TemplateResponse("learning.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def read_profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@app.get("/api")
async def root():
    return {"message": "Простое FastAPI приложение с OAuth2 и JWT"}