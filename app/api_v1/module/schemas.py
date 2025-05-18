from typing import List, Optional
from pydantic import BaseModel


class TopicBase(BaseModel):
    title: str
    description: Optional[str] = None
    order: int = 1


class TopicCreate(TopicBase):
    pass


class TopicUpdate(TopicBase):
    pass


class Topic(TopicBase):
    topic_id: int
    module_id: int

    class Config:
        orm_mode = True


class ModuleBase(BaseModel):
    title: str
    description: Optional[str] = None
    order: int = 1


class ModuleCreate(ModuleBase):
    pass


class ModuleUpdate(ModuleBase):
    pass


class Module(ModuleBase):
    module_id: int
    grade_id: int
    topics: List[Topic] = []

    class Config:
        orm_mode = True