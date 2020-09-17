from typing import Optional
from tortoise.contrib.pydantic import PydanticModel
from pydantic import Field, BaseModel
from core.shortcuts import (
    password_light_regex, password_light_msg_regex, email_regex)


class UserSchema(PydanticModel):
    name: Optional[str]
    username: str
    email: str = Field(..., regex=email_regex)
    password: Optional[str] = Field(
        None, regex=password_light_regex,
        description=password_light_msg_regex)
    avatar: Optional[str]
    is_active: bool = False
    is_admin: bool = False
    is_superuser: bool = False
    is_staff: bool = False

    class Config:
        orm_mode = True


class UserUpdateSchema(PydanticModel):
    name: Optional[str]
    avatar: Optional[str]
    is_active: bool = False
    is_admin: bool = False
    is_superuser: bool = False
    is_staff: bool = False

    class Config:
        orm_mode = True


class UserPasswordSchema(BaseModel):
    password: Optional[str] = Field(
        None, regex=password_light_regex,
        description=password_light_msg_regex)


class UserEmailSchema(BaseModel):
    email: str = Field(..., regex=email_regex)


class UserLoginSchema(BaseModel):
    email: str = Field(..., regex=email_regex)
    password: str = Field(
        ..., regex=password_light_regex,
        description=password_light_msg_regex)


class UserResetPasswordSchema(BaseModel):
    password: str = Field(
        ..., regex=password_light_regex,
        description=password_light_msg_regex)
    password2: str = Field(
        ..., regex=password_light_regex,
        description=password_light_msg_regex)


class UserRoleSchema(BaseModel):
    role: bool
