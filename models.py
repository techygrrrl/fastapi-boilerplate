from typing import Union

from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    description: str
    complete: bool