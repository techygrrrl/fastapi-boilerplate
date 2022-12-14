from typing import Union
from fastapi import Request

from app.db.database import SessionLocal
from app.db.queries import get_user
from app.models.schemas import UserBase


def get_current_user(request: Request, db: SessionLocal) -> Union[None, UserBase]:
    auth_header = request.headers.get("Authorization")
    if not auth_header: 
        return None

    token = auth_header.split("Bearer ")[1]
    print(">>>> Token: {}".format(token))

    # TODO: Perform user lookup
    user = get_user(db, token)
    print(">>>> user: {}".format(user))

    return user