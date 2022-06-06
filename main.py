from fastapi import FastAPI,HTTPException, Depends, Request
from pydantic import BaseModel
from typing import Optional,List
import schema
from database import Base, SessionLocal, engine
from model import Todo
from sqlalchemy.orm import session
from fastapi.responses import HTMLResponse
Base.metadata.create_all(bind=engine)
# def get_database_session():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

# # class Todo(BaseModel):
# #     name:str
# #     due_date:str
# #     description:str

# app=FastAPI(title="Todo Api")
# store_todo=[]
# @app.get("/")
# async def home():
#     return{"hello":"world"}

# @app.post('/todo/')
# async def create_todo(todo:Todo):
#     store_todo.append(todo)
#     return todo
# @app.get('/todo/',response_model=List[Todo])
# async def get_all_todos():
#     return store_todo

# @app.get('/todo/{id}')
# async def get_todo_by_id(id:int):
#     try:
#         return store_todo[id]
#     except:
#         raise HTTPException(status_code=404,detail="Todo not found")
# @app.put('/linux/{id}')
# async def update_todo(id:int,todo:Todo):
#     try:
#         store_todo[id]=todo
#         return store_todo[id]
#     except:
#         raise HTTPException(status_code=404,detail="Todo not found")
# @app.delete('/todo/{id}')
# async def delete_todo(id:int):
#     try:
#         obj=store_todo[id]
#         store_todo.pop(id)
#         return obj
#     except:
#         raise HTTPException(status_code=404,detail="Todo not found")



