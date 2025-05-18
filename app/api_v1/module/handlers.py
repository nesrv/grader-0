from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.api_v1.module.schemas import Module, Topic, ModuleCreate, ModuleUpdate, TopicCreate, TopicUpdate
from app.api_v1.module.service import (
    get_modules_by_grade,
    get_module,
    create_module,
    update_module,
    delete_module,
    get_topics_by_module,
    get_topic,
    create_topic,
    update_topic,
    delete_topic
)

router = APIRouter()


@router.get("/grade/{grade_id}/modules", response_model=List[Module])
def read_modules(grade_id: int, db: Session = Depends(get_db)):
    """
    Get all modules for a specific grade.
    """
    modules = get_modules_by_grade(db, grade_id)
    return modules


@router.get("/{module_id}", response_model=Module)
def read_module(module_id: int, db: Session = Depends(get_db)):
    """
    Get a specific module by ID.
    """
    module = get_module(db, module_id)
    if module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    return module


@router.post("/grade/{grade_id}/modules", response_model=Module, status_code=status.HTTP_201_CREATED)
def create_module_endpoint(grade_id: int, module: ModuleCreate, db: Session = Depends(get_db)):
    """
    Create a new module.
    """
    return create_module(db, module, grade_id)


@router.put("/{module_id}", response_model=Module)
def update_module_endpoint(module_id: int, module: ModuleUpdate, db: Session = Depends(get_db)):
    """
    Update an existing module.
    """
    updated_module = update_module(db, module_id, module)
    if updated_module is None:
        raise HTTPException(status_code=404, detail="Module not found")
    return updated_module


@router.delete("/{module_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_module_endpoint(module_id: int, db: Session = Depends(get_db)):
    """
    Delete a module.
    """
    success = delete_module(db, module_id)
    if not success:
        raise HTTPException(status_code=404, detail="Module not found")
    return None


@router.get("/{module_id}/topics", response_model=List[Topic])
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


@router.post("/{module_id}/topics", response_model=Topic, status_code=status.HTTP_201_CREATED)
def create_topic_endpoint(module_id: int, topic: TopicCreate, db: Session = Depends(get_db)):
    """
    Create a new topic.
    """
    return create_topic(db, topic, module_id)


@router.put("/topics/{topic_id}", response_model=Topic)
def update_topic_endpoint(topic_id: int, topic: TopicUpdate, db: Session = Depends(get_db)):
    """
    Update an existing topic.
    """
    updated_topic = update_topic(db, topic_id, topic)
    if updated_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return updated_topic


@router.delete("/topics/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_topic_endpoint(topic_id: int, db: Session = Depends(get_db)):
    """
    Delete a topic.
    """
    success = delete_topic(db, topic_id)
    if not success:
        raise HTTPException(status_code=404, detail="Topic not found")
    return None