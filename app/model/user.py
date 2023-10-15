from pydantic import BaseModel
from dataclasses import dataclass
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    password: str
    address: str
    is_admin: bool
    is_verified: bool

@dataclass
class UserRequestDTO:
    name: str
    surname: str
    email: str
    password: str
    address: str
    is_admin: bool
    is_verified: bool
    verification_code: Optional[str] = None
    
@dataclass
class UserResponseDTO:
    id: int
    name: str
    surname: str
    email: str
    address: str
    is_admin: bool
    is_verified: bool