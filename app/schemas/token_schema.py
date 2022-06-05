from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    id: str
    is_superuser: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None