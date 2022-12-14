from typing import Union

from fastapi import FastAPI

from models import Todo

app = FastAPI()

@app.get("/")
def root():
    return { "status": "ok" }

@app.get("/todo/{todo_id}")
def show_todo(todo_id: int, q: Union[str, None] = None):
    return { "id": todo_id, "q": q }

@app.post("/todo")
def create_todo(todo: Todo):
    return todo