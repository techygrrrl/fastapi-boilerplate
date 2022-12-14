from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from typing import Union

from app.db.database import Base

from pydantic import BaseModel

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, index=False)
    description = Column(String, index=False)
    completed = Column(Boolean)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, index=False)
