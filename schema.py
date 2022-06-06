from datetime import date
from pydantic import BaseModel
class Todo(BaseModel):
    name = str
    description=str
    due_date=str

    class Config:
        orm_mode = True