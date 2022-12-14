import time
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, Request
from app.auth.auth import get_current_user
from app.db.database import SessionLocal, get_db
from app.db.queries import create_todo, get_user

from app.models.schemas import TodoBase
from app.db.database import Base, engine


# import app.db.database as database

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
def root():
    return { "status": "ok" }

@app.get("/todo/{todo_id}")
def show_todo(todo_id: int, q: Union[str, None] = None):
    return { "id": todo_id, "q": q }

@app.post("/todo")
def post_todo(todo: TodoBase, request: Request, db: SessionLocal = Depends(get_db)):
    user = get_current_user(request, db)
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # print(">>>> create todo -> user: {}".format(user))

    created = create_todo(db, todo, user.id)

    return created