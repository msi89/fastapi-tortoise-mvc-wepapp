
from fastapi import APIRouter, Request
from core.services.auth import AuthService, model
from core.models.schemas.user import (
    UserSchema,
    UserUpdateSchema,
    UserLoginSchema,
    UserResetPasswordSchema,
    UserPasswordSchema
)
from typing import List
from starlette.status import HTTP_201_CREATED
from fastapi import Depends
from core.middlewares.auth import get_current_active_user
from core.shortcuts import view

router = APIRouter()

tags = ['accounts']


@router.get('/users')
async def get_users_list(request: Request, token: str = Depends(get_current_active_user)):
    users = await AuthService.get()
    return view(template='auth/users.html', context=users)


@router.get('/signup')
async def sign_up(request: Request):
    return view(template='auth/signup.html', context={"request": request}, request=request)


@router.post('/signup')
async def sign_save(request: Request, model: UserSchema):
    return await AuthService.create(model)


# @router.get('/{user_id}', response_model=model)
# async def get_user_by_id(user_id: int, token: str = Depends(get_current_active_user)):
#     return await AuthService.get(id=user_id)


# @router.put('/{user_id}', response_model=model)
# async def update_user_data(user_id: int, user: UserUpdateSchema, token: str = Depends(get_current_active_user)):
#     return await AuthService.update(user_id, user)


# @router.put('/{user_id}/reset_password', response_model=model)
# async def reset_user_password(user_id: int, data: UserPasswordSchema, token: str = Depends(get_current_active_user)):
#     return await AuthService.reset_user_password(user_id, data.password)


# @router.patch('/change_password', response_model=model)
# async def change_user_password(data: UserResetPasswordSchema, user: str = Depends(get_current_active_user)):
#     return await AuthService.change_password(data.password, data.password2, user)


# @router.patch('/current')
# async def current_user(user: str = Depends(get_current_active_user)):
#     return AuthService.get_current_user(user)


# @router.post('/signin')
# async def sign_in(data: UserLoginSchema):
#     return await AuthService.sign_in(data.email, data.password)
