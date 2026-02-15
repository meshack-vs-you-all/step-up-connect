from fastapi import APIRouter, Depends
from models import User
from api.deps import get_current_user
from pydantic import BaseModel

router = APIRouter()

class UserSchema(BaseModel):
    id: int
    email: str
    role: str
    
    class Config:
        orm_mode = True

@router.get("/me", response_model=UserSchema)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
