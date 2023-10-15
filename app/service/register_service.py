from fastapi import HTTPException, status, Request

from app.repository.user_repository import UserRepository
from app.model.register import RegisterDTO
from app.model.user import UserRequestDTO
from app.utils.validator import validate_email, validate_password_policy
from app.security.password_hasher import hash_password
from app.utils.mail_sender import MailSender
from app.model.email import Email
from app.security.activation_link_provider import *


class RegisterService:
    
    @staticmethod
    async def register(credentials: RegisterDTO, request: Request):
        await RegisterService.__validate_data(credentials)
        hashed_password = hash_password(credentials.password)
        data = generate_verification_data()
        user_data = UserRequestDTO(**{
            "name": credentials.name,
            "surname": credentials.surname,
            "email": credentials.email,
            "password": hashed_password,
            "address": credentials.address,
            "is_admin": credentials.is_admin,
            "is_verified": False,
            "verification_code": data["verification_code"]
        })
        await UserRepository.create_user(user_data)
        email_data = RegisterService.__create_registration_email(credentials, data["token"], request)
        await MailSender().send_verification_email(email_data)

    
    @staticmethod
    async def verify_account(token: str):
        verification_code = decrypt_verification_code_from_token(token)
        user = await UserRepository.get_user_by_verification_code(verification_code)
        if user is not None and user.is_verified is False:
            user.is_verified = True
            await UserRepository.update_user(user.id, user)
        elif user is not None and user.is_verified is True:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already verified.")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such user in database")

    
    # Private methods
    @staticmethod
    async def __validate_data(data: RegisterDTO):
        print(f"Entered validation! {data.email}, {data.password}")
        if not data.email or not data.password or not data.name or not data.surname or not data.address:
            print("Entered no data or password!")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        if validate_email(data.email) is False:
            print("Entered faulty email")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format. It should look like this name@example.domain")
        if await UserRepository.get_user_by_email(data.email) is not None:
            print("Entered dupolicate email")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with such email already exists.")
        if validate_password_policy(data.password) is False:
            print("Entered password is bebebebe email")
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Password does not confirms to security policy.")

    @staticmethod
    def __create_registration_email(data: RegisterDTO, token: str, request: Request) -> Email:
        print("Debug 0")
        email = Email(
            email=[data.email],
            body={
                "name": data.name,
                "surname": data.surname,
                "activation_link": generate_activation_link(token, request)
            }
        )
        print(f"DEBUG {email.body}, {email.email}")
        return email
        