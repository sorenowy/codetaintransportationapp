from pydantic import EmailStr, BaseModel
from typing import Any

class Email(BaseModel):
    email: list[EmailStr]
    body: dict[str, Any]
    