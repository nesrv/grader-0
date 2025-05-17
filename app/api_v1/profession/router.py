from fastapi import APIRouter, Depends
from typing import List, Dict

from app.api_v1.auth.handlers import get_current_active_user
from app.api_v1.profession.schemas import Profession, ProfessionCreate, ProfessionUpdate
from app.api_v1.profession.handlers import (
    read_professions, read_profession, create_new_profession,
    update_existing_profession, delete_existing_profession
)

router = APIRouter()

# Маршруты для профессий
router.add_api_route("", read_professions, methods=["GET"], response_model=List[Profession])
router.add_api_route("", create_new_profession, methods=["POST"], response_model=Profession, dependencies=[Depends(get_current_active_user)])
router.add_api_route("/{profession_id}", read_profession, methods=["GET"], response_model=Profession)
router.add_api_route("/{profession_id}", update_existing_profession, methods=["PUT"], response_model=Profession, dependencies=[Depends(get_current_active_user)])
router.add_api_route("/{profession_id}", delete_existing_profession, methods=["DELETE"], response_model=Dict[str, bool], dependencies=[Depends(get_current_active_user)])