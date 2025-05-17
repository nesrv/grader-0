from typing import Optional
from pydantic import BaseModel

class ProfessionBase(BaseModel):
    name: str
    description: Optional[str] = None
    image_path: Optional[str] = None

class ProfessionCreate(ProfessionBase):
    pass

class ProfessionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    image_path: Optional[str] = None

class Profession(ProfessionBase):
    profession_id: int

    class Config:
        orm_mode = True