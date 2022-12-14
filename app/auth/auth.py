from typing import Union
from fastapi import Request

from app.db.database import SessionLocal
from app.db.queries import get_user
from app.models.schemas import UserBase

"""
Util to get the current user based on the token in the Authorization header
"""
def get_current_user(request: Request, db: SessionLocal) -> Union[None, UserBase]:
    auth_header = request.headers.get("Authorization")
    if not auth_header: 
        return None

    token = auth_header.split("Bearer ")[1]

    return get_user(db, token)