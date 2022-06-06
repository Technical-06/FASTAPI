import imp
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base
from sqlalchemy import Column, PrimaryKeyConstraint, true
class Todo(Base):
    __tablename__ = "todo"
    id=Column(Integer,primary_key=True)
    name = Column(String(20), unique=True)
    description=Column(String(20), nullable=False)
    due_date=Column(String(20), nullable=False)