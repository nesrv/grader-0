from fastapi import APIRouter
from app.api_v1.module.handlers import router as module_router

router = APIRouter()
router.include_router(module_router)