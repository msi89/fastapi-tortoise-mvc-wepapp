
from core.models.auth import User
from tortoise.contrib.pydantic import pydantic_model_creator
from core.models.schemas.user import UserSchema, UserUpdateSchema
from core.middlewares.auth import (
    authenticate, create_access_token)
from core.middlewares.security import hash_password, verify_password
from core.exceptions import raise_authenticate, Http400

model = pydantic_model_creator(User)


class AuthService():

    async def get(id: int = None):
        User.all().prefetch_related()
        if(id is not None):
            return await model.from_queryset_single(User.get(id=id))
        return await model.from_queryset(User.all())

    async def create(user: UserSchema):
        user_obj = await User.create(**user.dict())
        return model.from_orm(user_obj)

    async def update(id: int, user: UserUpdateSchema):
        await User.filter(id=id).update(**user.dict(exclude_unset=True))
        return await model.from_queryset_single(User.get(id=id))

    async def sign_in(email: str, password: str):
        user = await authenticate(email, password)
        if not user:
            return raise_authenticate()
        token = create_access_token(data=user.__dict__)
        return {"access_token": token, "meta": model.from_orm(user)}

    async def reset_user_password(id: int, password: str) -> User:
        await User.filter(id=id).update(password=hash_password(password))
        return await model.from_queryset_single(User.get(id=id))

    async def change_password(old_password: str, password: str, user: User):
        if not verify_password(old_password, user.password):
            return Http400("Incorrect password")
        user.password = password
        await user.save()
        return model.from_orm(user)

    def get_current_user(user: User):
        return model.from_orm(user)
