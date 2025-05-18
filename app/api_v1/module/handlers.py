from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.api_v1.module.schemas import Module, Topic, ModuleCreate, TopicCreate
from app.api_v1.module.service import (
    get_modules_by_grade,
    get_module,
    create_module,
    get_topics_by_module,
    get_topic,
    create_topic
)

router = APIRouter()


@router.get("/grade/{grade_id}/modules", response_model=List[Module])
def read_modules(grade_id: int, db: Session = Depends(get_db)):
    """
    Get all modules for a specific grade.
    """
    modules = get_modules_by_grade(db, grade_id)
    return modules


@router.get("/modules/{module_id}", response_model=Module)
def read_module(module_id: int, db: Session = Depends(get_db)):
    """
    Get a specific module by ID.
    """
    module = get_module(db, module_id)
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    return module


@router.post("/grade/{grade_id}/modules", response_model=Module)
def create_module_endpoint(grade_id: int, module: ModuleCreate, db: Session = Depends(get_db)):
    """
    Create a new module.
    """
    return create_module(db, module, grade_id)


@router.get("/module/{module_id}/topics", response_model=List[Topic])
def read_topics(module_id: int, db: Session = Depends(get_db)):
    """
    Get all topics for a specific module.
    """
    topics = get_topics_by_module(db, module_id)
    return topics


@router.get("/topics/{topic_id}", response_model=Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    """
    Get a specific topic by ID.
    """
    topic = get_topic(db, topic_id)
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic


@router.post("/module/{module_id}/topics", response_model=Topic)
def create_topic_endpoint(module_id: int, topic: TopicCreate, db: Session = Depends(get_db)):
    """
    Create a new topic.
    """
    return create_topic(db, topic, module_id)