from fastapi import APIRouter, Depends, status
from app.api.v1.schema.schema import ResponseSchema
from app.service.user_service import UserService
from app.model.user import UserRequestDTO


users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_users():
    result = await UserService.get_all_users()
    return ResponseSchema(detail="SUCCESS", result=result)


@users_router.get("/{userId}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_user_by_id(userId: int):
    result = await UserService.get_user_by_id(userId)
    return ResponseSchema(detail="SUCCESS", result=result)


@users_router.post("", response_model=ResponseSchema, response_model_exclude_none=True, status_code=status.HTTP_200_OK)
async def create_user(user_data: UserRequestDTO):
    await UserService.create_user(user_data)
    return ResponseSchema(detail="SUCCESS")


@users_router.delete("/{userId}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_user(userId: int):
    await UserService.delete_user(userId)
    return ResponseSchema(detail="SUCCESS")


@users_router.patch("/{userId}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_user(user_data: UserRequestDTO, userId: int):
    await UserService.update_user(userId, user_data)
    return ResponseSchema(detail="SUCCESS")