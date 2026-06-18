from datetime import datetime, timedelta
from jose import jwt

from app.core.config import (
    SECRET_KEY,
    ALGORITHM
)

def create_access_token(data: dict):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow()
        + timedelta(hours=1)
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )