from typing import List, Optional
from pydantic import BaseModel


class TheoryBase(BaseModel):
    title: str
    description: Optional[str] = None
    code_question: Optional[str] = None
    is_active: bool = True


class TheoryCreate(TheoryBase):
    topic_id: int


class TheoryUpdate(TheoryBase):
    pass


class Theory(TheoryBase):
    theory_id: int
    topic_id: int

    class Config:
        orm_mode = True


class TopicBase(BaseModel):
    title: str
    description: Optional[str] = None
    order: int = 1


class TopicCreate(TopicBase):
    module_id: int


class TopicUpdate(TopicBase):
    pass


class Topic(TopicBase):
    topic_id: int
    module_id: int
    theories: List[Theory] = []

    class Config:
        orm_mode = True