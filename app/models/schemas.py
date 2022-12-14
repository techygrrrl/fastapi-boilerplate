from typing import List, Union

from pydantic import BaseModel


class TodoBase(BaseModel):
    name: str
    description: Union[str, None] = None
    completed: bool

# TODO: Learn more about schemas vs. models

class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    token: str
    todos: List[Todo] = []
    
    class Config:
        orm_mode = True