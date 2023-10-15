from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.api.v1.schema.schema import ResponseSchema
from app.service.register_service import RegisterService
from app.model.register import RegisterDTO
from app.model.email import Email

register_router = APIRouter(prefix="/register", tags=["Register"])

@register_router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def register(credentials: RegisterDTO, request: Request):
    await RegisterService.register(credentials, request)
    return ResponseSchema(detail="SUCCESS")

@register_router.get("/verify/{token}", response_model=ResponseSchema, response_model_exclude_none=True)
async def verify_user(token: str):
    print("REQUEST RECEIVED")
    await RegisterService.verify_account(token)
    return RedirectResponse("https://wp.pl")