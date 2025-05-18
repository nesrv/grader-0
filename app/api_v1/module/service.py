from typing import List, Optional
from sqlalchemy.orm import Session

from app.api_v1.module.models import Module, Topic
from app.api_v1.module.schemas import ModuleCreate, ModuleUpdate, TopicCreate, TopicUpdate


def get_modules_by_grade(db: Session, grade_id: int) -> List[Module]:
    """
    Get all modules for a specific grade.
    """
    return db.query(Module).filter(Module.grade_id == grade_id).order_by(Module.order).all()


def get_module(db: Session, module_id: int) -> Optional[Module]:
    """
    Get a specific module by ID.
    """
    return db.query(Module).filter(Module.module_id == module_id).first()


def create_module(db: Session, module: ModuleCreate, grade_id: int) -> Module:
    """
    Create a new module.
    """
    db_module = Module(**module.dict(), grade_id=grade_id)
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module


def update_module(db: Session, module_id: int, module: ModuleUpdate) -> Optional[Module]:
    """
    Update an existing module.
    """
    db_module = get_module(db, module_id)
    if db_module:
        for key, value in module.dict(exclude_unset=True).items():
            setattr(db_module, key, value)
        db.commit()
        db.refresh(db_module)
    return db_module


def delete_module(db: Session, module_id: int) -> bool:
    """
    Delete a module.
    """
    db_module = get_module(db, module_id)
    if db_module:
        db.delete(db_module)
        db.commit()
        return True
    return False


def get_topics_by_module(db: Session, module_id: int) -> List[Topic]:
    """
    Get all topics for a specific module.
    """
    return db.query(Topic).filter(Topic.module_id == module_id).order_by(Topic.order).all()


def get_topic(db: Session, topic_id: int) -> Optional[Topic]:
    """
    Get a specific topic by ID.
    """
    return db.query(Topic).filter(Topic.topic_id == topic_id).first()


def create_topic(db: Session, topic: TopicCreate, module_id: int) -> Topic:
    """
    Create a new topic.
    """
    db_topic = Topic(**topic.dict(), module_id=module_id)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic


def update_topic(db: Session, topic_id: int, topic: TopicUpdate) -> Optional[Topic]:
    """
    Update an existing topic.
    """
    db_topic = get_topic(db, topic_id)
    if db_topic:
        for key, value in topic.dict(exclude_unset=True).items():
            setattr(db_topic, key, value)
        db.commit()
        db.refresh(db_topic)
    return db_topic


def delete_topic(db: Session, topic_id: int) -> bool:
    """
    Delete a topic.
    """
    db_topic = get_topic(db, topic_id)
    if db_topic:
        db.delete(db_topic)
        db.commit()
        return True
    return False