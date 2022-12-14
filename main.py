import time
from typing import Union

from fastapi import FastAPI, Request

from models import Todo

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.middleware("http")
async def authenticate_user(request: Request, call_next):
    response = await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header: 
        return response
    
    token = auth_header.split("Bearer ")[1]
    print(">>>> Token: {}".format(token))

    # TODO: Perform user lookup

    return response

@app.get("/")
def root():
    return { "status": "ok" }

@app.get("/todo/{todo_id}")
def show_todo(todo_id: int, q: Union[str, None] = None):
    return { "id": todo_id, "q": q }

@app.post("/todo")
def create_todo(todo: Todo):
    return todo