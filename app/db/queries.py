from app.db.database import SessionLocal
from app.models.models import Todo, User


def get_user(db: SessionLocal, token: str):
    return db.query(User).filter(User.token == token).first()

def create_todo(db: SessionLocal, todo: Todo, user_id: int):
    db_todo = Todo(name=todo.name, description=todo.description, owner_id=user_id, completed=False)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo