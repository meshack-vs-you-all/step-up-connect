from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class UserRole(str, Enum):
    YOUTH = "youth"
    MENTOR = "mentor"
    SME = "sme"
    ADMIN = "admin"

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    role: UserRole = UserRole.YOUTH

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    role: Optional[str] = None
