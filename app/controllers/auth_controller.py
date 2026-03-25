from fastapi import APIRouter, Depends
from app.schemas.auth_schema import LoginRequest
from app.services import auth_service
from app.config.db import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(data: LoginRequest, db=Depends(get_db)):
    return auth_service.login(db, data.username, data.password)