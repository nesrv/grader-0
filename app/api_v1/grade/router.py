from fastapi import APIRouter, Depends
from typing import List, Dict

from app.api_v1.auth.handlers import get_current_active_user
from app.api_v1.grade.schemas import Grade, GradeCreate, GradeUpdate
from app.api_v1.grade.handlers import (
    read_grades, read_grade, read_grades_by_profession,
    create_new_grade, update_existing_grade, delete_existing_grade
)

router = APIRouter()

# Маршруты для грейдов
router.add_api_route("", read_grades, methods=["GET"], response_model=List[Grade])
router.add_api_route("", create_new_grade, methods=["POST"], response_model=Grade, dependencies=[Depends(get_current_active_user)])
router.add_api_route("/{grade_id}", read_grade, methods=["GET"], response_model=Grade)
router.add_api_route("/{grade_id}", update_existing_grade, methods=["PUT"], response_model=Grade, dependencies=[Depends(get_current_active_user)])
router.add_api_route("/{grade_id}", delete_existing_grade, methods=["DELETE"], response_model=Dict[str, bool], dependencies=[Depends(get_current_active_user)])
router.add_api_route("/profession/{profession_id}", read_grades_by_profession, methods=["GET"], response_model=List[Grade])