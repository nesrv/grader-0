from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.orm import relationship

from app.database import Base, Topic


class Theory(Base):
    __tablename__ = "theory"
    
    theory_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    answer_type = Column(Enum("understand", "not_understand", name="answer_type_enum"), nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Связь с темой
    topic_id = Column(Integer, ForeignKey("topics.topic_id"), nullable=False)
    topic = relationship("Topic", back_populates="theories")


class Question(Base):
    __tablename__ = "questions"
    
    question_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    options = Column(JSON, nullable=False)  # Варианты ответов в JSON
    correct_answers = Column(JSON, nullable=False)  # Индексы правильных ответов
    is_active = Column(Boolean, default=True)
    
    # Связь с темой
    topic_id = Column(Integer, ForeignKey("topics.topic_id"), nullable=False)
    topic = relationship("Topic", back_populates="questions")


class Task(Base):
    __tablename__ = "tasks"
    
    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    code_question = Column(Text, nullable=False)
    correct_answer = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Связь с темой
    topic_id = Column(Integer, ForeignKey("topics.topic_id"), nullable=False)
    topic = relationship("Topic", back_populates="tasks")


class Case(Base):
    __tablename__ = "cases"
    
    case_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    code_template = Column(Text, nullable=False)
    correct_fields = Column(JSON, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Связь с темой
    topic_id = Column(Integer, ForeignKey("topics.topic_id"), nullable=False)
    topic = relationship("Topic", back_populates="cases")