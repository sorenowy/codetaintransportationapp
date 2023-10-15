from app.repository.user_repository import UserRepository
from app.model.login import LoginDTO
from fastapi import HTTPException, status
from app.security.password_hasher import read_hashed_password
from app.security.authorization import Session

class LoginService:
    
    @staticmethod
    async def login(credentials: LoginDTO, session: Session) -> int:
        user = await UserRepository.get_user_by_email(credentials.email)
        if user is None or read_hashed_password(credentials.password, user.password) is False:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
        print("TODO BUT IT WORKS FINE!")
        session.create_session("ABC", user.id)
        return { "token": "ABC" }
            # make an JWT with payload of userDTO.
            
    @staticmethod
    async def logout(session: Session):
        session.clear_session()
        # delete JWT token, i think :)