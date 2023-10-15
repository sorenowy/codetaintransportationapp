from dataclasses import dataclass

@dataclass
class RegisterDTO:
    email: str
    password: str
    name: str
    surname: str
    address: str
    is_admin: bool