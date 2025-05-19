from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import enum

SQLALCHEMY_DATABASE_URL = "sqlite:///./grader.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)

class GradeLevel(enum.Enum):
    """
    Grade level enum.
    """
    STAGER = "intern"
    JUNIOR = "junior"
    JUNIOR_PLUS = "junior+"
    MIDDLE = "middle"
    SENIOR = "senior"
   
    # STAGER = "стажер"
    # JUNIOR = "джун"
    # JUNIOR_PLUS = "джун+"
    # MIDDLE = "мидл"
    # SENIOR = "сениор"
    

# Define Profession model here to ensure it's created with Base.metadata.create_all
class Profession(Base):
    __tablename__ = "professions"
    profession_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    image_path = Column(String, nullable=True)
    
    # Relations
    grades = relationship("Grade", back_populates="profession")

class Grade(Base):
    __tablename__ = "grades"
    grade_id = Column(Integer, primary_key=True, index=True)
    level_name = Column(Enum(GradeLevel), nullable=False, default=GradeLevel.JUNIOR)
    description = Column(Text, nullable=True)
    
    # Relations
    profession_id = Column(Integer, ForeignKey("professions.profession_id"), nullable=False)
    profession = relationship("Profession", back_populates="grades")
    
    # One-to-many relationship with modules
    modules = relationship("Module", back_populates="grade", cascade="all, delete-orphan")

# Module model
class Module(Base):
    __tablename__ = "modules"
    
    module_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, nullable=False, default=1)
    
    # Relations
    grade_id = Column(Integer, ForeignKey("grades.grade_id"), nullable=False)
    grade = relationship("Grade", back_populates="modules")
    
    # One-to-many relationship with topics
    topics = relationship("Topic", back_populates="module", cascade="all, delete-orphan")

# Topic model
class Topic(Base):
    __tablename__ = "topics"
    
    topic_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, nullable=False, default=1)
    
    # Relations
    module_id = Column(Integer, ForeignKey("modules.module_id"), nullable=False)
    module = relationship("Module", back_populates="topics")
    
    # Обратные связи для учебных материалов
    theories = relationship("Theory", back_populates="topic", cascade="all, delete-orphan")
    questions = relationship("Question", back_populates="topic", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="topic", cascade="all, delete-orphan")
    cases = relationship("Case", back_populates="topic", cascade="all, delete-orphan")

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()