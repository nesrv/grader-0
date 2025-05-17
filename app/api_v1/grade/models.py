import enum
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class GradeLevel(enum.Enum):
    """
    Grade level enum.
    """
    STAGER = "intern"
    JUNIOR = "junior"
    JUNIOR_PLUS = "junior+"
    MIDDLE = "middle"
    SENIOR = "senior"

class Grade(Base):
    __tablename__ = "grades"
    grade_id = Column(Integer, primary_key=True, index=True)
    level_name = Column(Enum(GradeLevel), nullable=False, default=GradeLevel.JUNIOR)
    description = Column(Text, nullable=True)
    
    # Relations
    profession_id = Column(Integer, ForeignKey("professions.profession_id"), nullable=False)
    profession = relationship("Profession", back_populates="grades")