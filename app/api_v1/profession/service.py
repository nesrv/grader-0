from typing import List, Optional
from sqlalchemy.orm import Session

from app.api_v1.profession.models import Profession
from app.api_v1.profession.schemas import ProfessionCreate, ProfessionUpdate

def get_profession(db: Session, profession_id: int) -> Optional[Profession]:
    return db.query(Profession).filter(Profession.profession_id == profession_id).first()

def get_professions(db: Session, skip: int = 0, limit: int = 100) -> List[Profession]:
    return db.query(Profession).offset(skip).limit(limit).all()

def create_profession(db: Session, profession: ProfessionCreate) -> Profession:
    db_profession = Profession(**profession.dict())
    db.add(db_profession)
    db.commit()
    db.refresh(db_profession)
    return db_profession

def update_profession(db: Session, profession_id: int, profession: ProfessionUpdate) -> Optional[Profession]:
    db_profession = get_profession(db, profession_id)
    if db_profession is None:
        return None
    
    update_data = profession.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_profession, key, value)
    
    db.commit()
    db.refresh(db_profession)
    return db_profession

def delete_profession(db: Session, profession_id: int) -> bool:
    db_profession = get_profession(db, profession_id)
    if db_profession is None:
        return False
    
    db.delete(db_profession)
    db.commit()
    return True