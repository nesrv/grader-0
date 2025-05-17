from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.api_v1.auth.handlers import get_current_active_user
from app.api_v1.auth.models import User
from app.api_v1.grade.schemas import Grade, GradeCreate, GradeUpdate
from app.api_v1.grade.service import (
    get_grade,
    get_grades,
    get_grades_by_profession,
    create_grade,
    update_grade,
    delete_grade
)

async def read_grades(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    grades = get_grades(db, skip=skip, limit=limit)
    return grades

async def read_grade(
    grade_id: int,
    db: Session = Depends(get_db)
):
    db_grade = get_grade(db, grade_id=grade_id)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade

async def read_grades_by_profession(
    profession_id: int,
    db: Session = Depends(get_db)
):
    grades = get_grades_by_profession(db, profession_id=profession_id)
    return grades

async def create_new_grade(
    grade: GradeCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return create_grade(db=db, grade=grade)

async def update_existing_grade(
    grade_id: int,
    grade: GradeUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_grade = update_grade(db, grade_id, grade)
    if db_grade is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade

async def delete_existing_grade(
    grade_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    success = delete_grade(db, grade_id)
    if not success:
        raise HTTPException(status_code=404, detail="Grade not found")
    return {"ok": True}