from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas


def get_topic(db: Session, topic_id: int):
    return db.query(models.Topic).filter(models.Topic.topic_id == topic_id).first()


def get_topics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).offset(skip).limit(limit).all()


def create_topic(db: Session, topic: schemas.TopicCreate):
    db_topic = models.Topic(**topic.dict())
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic


def update_topic(db: Session, topic_id: int, topic: schemas.TopicUpdate):
    db_topic = db.query(models.Topic).filter(models.Topic.topic_id == topic_id).first()
    if db_topic:
        for key, value in topic.dict().items():
            setattr(db_topic, key, value)
        db.commit()
        db.refresh(db_topic)
    return db_topic


def delete_topic(db: Session, topic_id: int):
    db_topic = db.query(models.Topic).filter(models.Topic.topic_id == topic_id).first()
    if db_topic:
        db.delete(db_topic)
        db.commit()
        return True
    return False


# CRUD для Theory
def get_theory(db: Session, theory_id: int):
    return db.query(models.Theory).filter(models.Theory.theory_id == theory_id).first()


def get_theories_by_topic(db: Session, topic_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Theory).filter(models.Theory.topic_id == topic_id).offset(skip).limit(limit).all()


def create_theory(db: Session, theory: schemas.TheoryCreate):
    db_theory = models.Theory(**theory.dict())
    db.add(db_theory)
    db.commit()
    db.refresh(db_theory)
    return db_theory


def update_theory(db: Session, theory_id: int, theory: schemas.TheoryUpdate):
    db_theory = db.query(models.Theory).filter(models.Theory.theory_id == theory_id).first()
    if db_theory:
        for key, value in theory.dict().items():
            setattr(db_theory, key, value)
        db.commit()
        db.refresh(db_theory)
    return db_theory


def delete_theory(db: Session, theory_id: int):
    db_theory = db.query(models.Theory).filter(models.Theory.theory_id == theory_id).first()
    if db_theory:
        db.delete(db_theory)
        db.commit()
        return True
    return False


def create_theories_list(db: Session, topic_id: int, theories_list: List[schemas.TheoryBase]):
    created_theories = []
    for theory_data in theories_list:
        theory_create = schemas.TheoryCreate(**theory_data.dict(), topic_id=topic_id)
        db_theory = models.Theory(**theory_create.dict())
        db.add(db_theory)
        created_theories.append(db_theory)
    
    db.commit()
    for theory in created_theories:
        db.refresh(theory)
    
    return created_theories