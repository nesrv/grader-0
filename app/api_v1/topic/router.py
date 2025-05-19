from fastapi import APIRouter
from . import handlers

router = APIRouter(
    prefix="/topic",
    tags=["topic"],
)

router.include_router(handlers.router)