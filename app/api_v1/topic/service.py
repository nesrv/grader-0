from typing import List, Dict, Any
from sqlalchemy.orm import Session

from . import models, schemas


def create_theory(db: Session, theory: schemas.TheoryCreate):
    db_theory = models.Theory(**theory.dict())
    db.add(db_theory)
    db.commit()
    db.refresh(db_theory)
    return db_theory


def get_theories_by_topic(db: Session, topic_id: int):
    return db.query(models.Theory).filter(
        models.Theory.topic_id == topic_id, 
        models.Theory.is_active == True
    ).all()


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_questions_by_topic(db: Session, topic_id: int):
    return db.query(models.Question).filter(
        models.Question.topic_id == topic_id, 
        models.Question.is_active == True
    ).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks_by_topic(db: Session, topic_id: int):
    return db.query(models.Task).filter(
        models.Task.topic_id == topic_id, 
        models.Task.is_active == True
    ).all()


def create_case(db: Session, case: schemas.CaseCreate):
    db_case = models.Case(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case


def get_cases_by_topic(db: Session, topic_id: int):
    return db.query(models.Case).filter(
        models.Case.topic_id == topic_id, 
        models.Case.is_active == True
    ).all()


def get_all_topic_materials(db: Session, topic_id: int):
    theories = get_theories_by_topic(db, topic_id)
    questions = get_questions_by_topic(db, topic_id)
    tasks = get_tasks_by_topic(db, topic_id)
    cases = get_cases_by_topic(db, topic_id)
    
    return {
        "theories": theories,
        "questions": questions,
        "tasks": tasks,
        "cases": cases
    }