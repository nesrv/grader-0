from typing import List, Optional
from pydantic import BaseModel


class TheoryBase(BaseModel):
    title: str
    answer_type: str
    is_active: bool = True


class TheoryCreate(TheoryBase):
    topic_id: int


class Theory(TheoryBase):
    theory_id: int
    topic_id: int
    
    class Config:
        from_attributes = True


class QuestionBase(BaseModel):
    title: str
    options: List[str]
    correct_answers: List[int]
    is_active: bool = True


class QuestionCreate(QuestionBase):
    topic_id: int


class Question(QuestionBase):
    question_id: int
    topic_id: int
    
    class Config:
        from_attributes = True


class TaskBase(BaseModel):
    title: str
    code_question: str
    correct_answer: str
    is_active: bool = True


class TaskCreate(TaskBase):
    topic_id: int


class Task(TaskBase):
    task_id: int
    topic_id: int
    
    class Config:
        from_attributes = True


class CaseBase(BaseModel):
    title: str
    code_template: str
    correct_fields: List[str]
    is_active: bool = True


class CaseCreate(CaseBase):
    topic_id: int


class Case(CaseBase):
    case_id: int
    topic_id: int
    
    class Config:
        from_attributes = True