from typing import List, Optional
from sqlalchemy.orm import Session

from app.database import Grade
from app.api_v1.grade.schemas import GradeCreate, GradeUpdate

def get_grade(db: Session, grade_id: int) -> Optional[Grade]:
    return db.query(Grade).filter(Grade.grade_id == grade_id).first()

def get_grades(db: Session, skip: int = 0, limit: int = 100) -> List[Grade]:
    return db.query(Grade).offset(skip).limit(limit).all()

def get_grades_by_profession(db: Session, profession_id: int) -> List[Grade]:
    return db.query(Grade).filter(Grade.profession_id == profession_id).all()

def create_grade(db: Session, grade: GradeCreate) -> Grade:
    db_grade = Grade(
        level_name=grade.level_name,
        description=grade.description,
        profession_id=grade.profession_id
    )
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

def update_grade(db: Session, grade_id: int, grade: GradeUpdate) -> Optional[Grade]:
    db_grade = get_grade(db, grade_id)
    if db_grade is None:
        return None
    
    update_data = grade.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_grade, key, value)
    
    db.commit()
    db.refresh(db_grade)
    return db_grade

def delete_grade(db: Session, grade_id: int) -> bool:
    db_grade = get_grade(db, grade_id)
    if db_grade is None:
        return False
    
    db.delete(db_grade)
    db.commit()
    return True