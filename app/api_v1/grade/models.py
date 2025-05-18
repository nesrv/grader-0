import enum
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base, GradeLevel

# Grade model is already defined in database.py, so we don't need to redefine it here
# Just import it from database.py
from app.database import Grade