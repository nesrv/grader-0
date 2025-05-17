from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

class GradeLevelEnum(str, Enum):
    STAGER = "intern"
    JUNIOR = "junior"
    JUNIOR_PLUS = "junior+"
    MIDDLE = "middle"
    SENIOR = "senior"

class GradeBase(BaseModel):
    level_name: GradeLevelEnum
    description: Optional[str] = None
    profession_id: int

class GradeCreate(GradeBase):
    pass

class GradeUpdate(BaseModel):
    level_name: Optional[GradeLevelEnum] = None
    description: Optional[str] = None
    profession_id: Optional[int] = None

class Grade(GradeBase):
    grade_id: int

    class Config:
        orm_mode = True