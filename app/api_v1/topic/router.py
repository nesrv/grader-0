from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from . import schemas, service

router = APIRouter()


@router.get("/topics/", response_model=List[schemas.Topic])
def read_topics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    topics = service.get_topics(db, skip=skip, limit=limit)
    return topics


@router.post("/topics/", response_model=schemas.Topic, status_code=status.HTTP_201_CREATED)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    return service.create_topic(db=db, topic=topic)


@router.get("/topics/{topic_id}", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic


@router.put("/topics/{topic_id}", response_model=schemas.Topic)
def update_topic(topic_id: int, topic: schemas.TopicUpdate, db: Session = Depends(get_db)):
    db_topic = service.update_topic(db, topic_id=topic_id, topic=topic)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic


@router.delete("/topics/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_topic(topic_id: int, db: Session = Depends(get_db)):
    success = service.delete_topic(db, topic_id=topic_id)
    if not success:
        raise HTTPException(status_code=404, detail="Topic not found")
    return None


# Маршруты для Theory
@router.get("/topics/{topic_id}/theories/", response_model=List[schemas.TheoryResponse])
def read_theories(topic_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Проверяем существование темы
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    theories = service.get_theories_by_topic(db, topic_id=topic_id, skip=skip, limit=limit)
    return theories


@router.post("/topics/{topic_id}/theories/", response_model=schemas.TheoryResponse, status_code=status.HTTP_201_CREATED)
def create_theory(topic_id: int, theory: schemas.TheoryBase, db: Session = Depends(get_db)):
    # Проверяем существование темы
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Создаем объект TheoryCreate с topic_id
    theory_create = schemas.TheoryCreate(**theory.dict(), topic_id=topic_id)
    return service.create_theory(db=db, theory=theory_create)


@router.get("/topics/{topic_id}/theories/{theory_id}", response_model=schemas.TheoryResponse)
def read_theory(topic_id: int, theory_id: int, db: Session = Depends(get_db)):
    # Проверяем существование темы
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    db_theory = service.get_theory(db, theory_id=theory_id)
    if db_theory is None or db_theory.topic_id != topic_id:
        raise HTTPException(status_code=404, detail="Theory not found for this topic")
    return db_theory


@router.put("/topics/{topic_id}/theories/{theory_id}", response_model=schemas.TheoryResponse)
def update_theory(topic_id: int, theory_id: int, theory: schemas.TheoryUpdate, db: Session = Depends(get_db)):
    # Проверяем существование темы
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Проверяем существование теории и принадлежность к теме
    db_theory = service.get_theory(db, theory_id=theory_id)
    if db_theory is None or db_theory.topic_id != topic_id:
        raise HTTPException(status_code=404, detail="Theory not found for this topic")
    
    updated_theory = service.update_theory(db, theory_id=theory_id, theory=theory)
    return updated_theory


@router.delete("/topics/{topic_id}/theories/{theory_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_theory(topic_id: int, theory_id: int, db: Session = Depends(get_db)):
    # Проверяем существование темы
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Проверяем существование теории и принадлежность к теме
    db_theory = service.get_theory(db, theory_id=theory_id)
    if db_theory is None or db_theory.topic_id != topic_id:
        raise HTTPException(status_code=404, detail="Theory not found for this topic")
    
    success = service.delete_theory(db, theory_id=theory_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete theory")
    return None


@router.post("/topics/{topic_id}/list_theories/", response_model=List[schemas.TheoryResponse], status_code=status.HTTP_201_CREATED)
def create_theories_list(topic_id: int, theories: List[schemas.TheoryBase], db: Session = Depends(get_db)):
    # Проверяем существование темы
    db_topic = service.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    # Создаем список теорий
    created_theories = service.create_theories_list(db=db, topic_id=topic_id, theories_list=theories)
    return created_theories