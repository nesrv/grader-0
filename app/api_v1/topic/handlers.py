from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from . import schemas, service

router = APIRouter()


@router.post("/theories/", response_model=schemas.Theory)
def create_theory(theory: schemas.TheoryCreate, db: Session = Depends(get_db)):
    return service.create_theory(db=db, theory=theory)


@router.get("/topics/{topic_id}/theories/", response_model=List[schemas.Theory])
def read_theories_by_topic(topic_id: int, db: Session = Depends(get_db)):
    return service.get_theories_by_topic(db=db, topic_id=topic_id)


@router.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return service.create_question(db=db, question=question)


@router.get("/topics/{topic_id}/questions/", response_model=List[schemas.Question])
def read_questions_by_topic(topic_id: int, db: Session = Depends(get_db)):
    return service.get_questions_by_topic(db=db, topic_id=topic_id)


@router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return service.create_task(db=db, task=task)


@router.get("/topics/{topic_id}/tasks/", response_model=List[schemas.Task])
def read_tasks_by_topic(topic_id: int, db: Session = Depends(get_db)):
    return service.get_tasks_by_topic(db=db, topic_id=topic_id)


@router.post("/cases/", response_model=schemas.Case)
def create_case(case: schemas.CaseCreate, db: Session = Depends(get_db)):
    return service.create_case(db=db, case=case)


@router.get("/topics/{topic_id}/cases/", response_model=List[schemas.Case])
def read_cases_by_topic(topic_id: int, db: Session = Depends(get_db)):
    return service.get_cases_by_topic(db=db, topic_id=topic_id)


@router.get("/topics/{topic_id}/materials/")
def read_all_topic_materials(topic_id: int, db: Session = Depends(get_db)):
    return service.get_all_topic_materials(db=db, topic_id=topic_id)