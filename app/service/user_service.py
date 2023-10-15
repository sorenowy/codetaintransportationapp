from fastapi import HTTPException, status

from app.repository.user_repository import UserRepository
from app.model.user import User, UserRequestDTO, UserResponseDTO
from app.utils.validator import validate_email, validate_password_policy
from app.security.password_hasher import hash_password


class UserService:
    
    @staticmethod
    async def get_all_users():
        return await UserRepository.get_all_users()

    @staticmethod
    async def get_user_by_id(id: int):
        result = await UserRepository.get_user_by_id(id)
        if result is not None:
            return UserResponseDTO(**{
                'id':result.id,
                'name':result.name,
                'surname':result.surname,
                'email':result.email,
                'address':result.address,
                'is_admin':result.is_admin,
                'is_verified':result.is_verified
            })   
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such user in database")
            

    @staticmethod
    async def create_user(data: UserRequestDTO):
        await UserService.__validate_data(data)
        hashed_password = hash_password(data.password)
        data.password = hashed_password
        return await UserRepository.create_user(data)

    @staticmethod
    async def delete_user(id: int):
        return await UserRepository.delete_user(id)

    @staticmethod
    async def update_user(id: int, data: User):
        return await UserRepository.update_user(id, data)

    @staticmethod
    async def __validate_data(data: UserRequestDTO):
        print(f"Entered validation! {data.email}, {data.password}")
        if not data.email or not data.password:
            print("Entered no email or password!")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        if validate_email(data.email) is False:
            print("Entered faulty email")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format. It should look like this name@example.domain")
        if await UserRepository.get_user_by_email(data.email) is not None:
            print("Entered duplicate email")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with such email already exists.")
        if validate_password_policy(data.password) is False:
            print("password is no no")
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Password does not confirms to security policy.")