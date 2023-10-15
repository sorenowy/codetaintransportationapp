from app.database.config.connection import prisma_connection
from app.model.user import User, UserRequestDTO

class UserRepository:
    
    @staticmethod
    async def get_all_users():
        return await prisma_connection.prisma.user.find_many()
    
    @staticmethod
    async def create_user(user: UserRequestDTO):
        return await prisma_connection.prisma.user.create({
            "name": user.name,
            "surname": user.surname,
            "email": user.email,
            "password": user.password,
            "address": user.address,
            "is_admin": user.is_admin,
            "is_verified": user.is_verified,
            "verification_code": user.verification_code
        })
        
    @staticmethod
    async def get_user_by_email(email: str):
        return await prisma_connection.prisma.user.find_first(where = { "email": email })
        
    @staticmethod
    async def get_user_by_id(id: int):
        return await prisma_connection.prisma.user.find_first(where = { "id": id })
    
    @staticmethod
    async def get_user_by_verification_code(code: str):
        return await prisma_connection.prisma.user.find_first(where= { "verification_code": code })
    
    @staticmethod
    async def delete_user(id: int):
        await prisma_connection.prisma.user.delete(where = { "id": id })
        
    @staticmethod
    async def update_user(id: int, user: UserRequestDTO):
        await prisma_connection.prisma.user.update(where = { "id": id }, data = {
            "name": user.name,
            "surname": user.surname,
            "email": user.email,
            "password": user.password,
            "address": user.address,
            "is_admin": user.is_admin,
            "is_verified": user.is_verified
        })