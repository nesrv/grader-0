from fastapi import APIRouter

from app.api_v1.home.handlers import get_home_page_data
from app.api_v1.home.schemas import HomePageData

router = APIRouter()

# Маршрут для получения данных главной страницы
router.add_api_route("", get_home_page_data, methods=["GET"], response_model=HomePageData)