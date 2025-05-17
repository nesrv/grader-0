from typing import List
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.api_v1.auth.handlers import get_current_active_user
from app.api_v1.auth.models import User
from app.api_v1.profession.schemas import Profession, ProfessionCreate, ProfessionUpdate
from app.api_v1.profession.service import (
    get_profession,
    get_professions,
    create_profession,
    update_profession,
    delete_profession
)

async def read_professions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    professions = get_professions(db, skip=skip, limit=limit)
    return professions

async def read_profession(
    profession_id: int,
    db: Session = Depends(get_db)
):
    db_profession = get_profession(db, profession_id=profession_id)
    if db_profession is None:
        raise HTTPException(status_code=404, detail="Profession not found")
    return db_profession

async def create_new_profession(
    profession: ProfessionCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    return create_profession(db=db, profession=profession)

async def update_existing_profession(
    profession_id: int,
    profession: ProfessionUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    db_profession = update_profession(db, profession_id, profession)
    if db_profession is None:
        raise HTTPException(status_code=404, detail="Profession not found")
    return db_profession

async def delete_existing_profession(
    profession_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    success = delete_profession(db, profession_id)
    if not success:
        raise HTTPException(status_code=404, detail="Profession not found")
    return {"ok": True}