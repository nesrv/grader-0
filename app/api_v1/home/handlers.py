from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.api_v1.profession.service import get_professions
from app.api_v1.grade.service import get_grades_by_profession
from app.api_v1.home.schemas import ProfessionWithGrades, HomePageData

async def get_home_page_data(db: Session = Depends(get_db)):
    # Получаем все профессии
    professions = get_professions(db)
    
    # Для каждой профессии получаем грейды
    professions_with_grades = []
    for profession in professions:
        grades = get_grades_by_profession(db, profession.profession_id)
        professions_with_grades.append(
            ProfessionWithGrades(
                profession=profession,
                grades=grades
            )
        )
    
    # Возвращаем данные для главной страницы
    return HomePageData(professions=professions_with_grades)