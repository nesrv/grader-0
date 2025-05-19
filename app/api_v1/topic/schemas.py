from typing import List, Optional, Any, Dict, Union
from pydantic import BaseModel


class TheoryBase(BaseModel):
    title: str
    description: Optional[str] = None
    code_question: Optional[str] = None
    text_question: Optional[str] = None
    variants: Optional[Dict[str, Any]] = None
    answer: Optional[List[str]] = None
    is_active: bool = True


class TheoryCreate(TheoryBase):
    topic_id: int


class TheoryUpdate(TheoryBase):
    pass


class TheoryResponse(BaseModel):
    theory_id: int
    title: str
    description: Optional[str] = None
    code_question: Optional[str] = None
    text_question: Optional[str] = None
    variants: Optional[Dict[str, Any]] = None
    answer: Optional[List[str]] = None
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
    theories: List[TheoryResponse] = []

    class Config:
        orm_mode = True