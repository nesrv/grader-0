from typing import List, Optional
from pydantic import BaseModel

from app.api_v1.profession.schemas import Profession
from app.api_v1.grade.schemas import Grade

class ProfessionWithGrades(BaseModel):
    profession: Profession
    grades: List[Grade]

class HomePageData(BaseModel):
    professions: List[ProfessionWithGrades]