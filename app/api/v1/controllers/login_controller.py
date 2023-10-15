from fastapi import APIRouter, Path, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.api.v1.schema.schema import ResponseSchema
from app.service.login_service import LoginService
from app.model.login import LoginDTO
from app.security.authorization import session

login_router = APIRouter(prefix="/login", tags=["Login"])

@login_router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def login(credentials: LoginDTO):
    result = await LoginService.login(credentials, session)
    return ResponseSchema(detail="SUCCESS", result=result)

@login_router.post("/logout", response_model=ResponseSchema, response_model_exclude_none=True)
async def logout():
    await LoginService.logout(session) # define token removal??
    print(session.__dict__.values())
    return ResponseSchema(detail="SUCCESS")