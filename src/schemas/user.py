import datetime

from pydantic import BaseModel, field_validator

from schemas.base import DefaultResponse
from utils.password_utils import get_password_hash


class BaseUserSchema(BaseModel):
    username: str


class CreateUserSchema(BaseUserSchema):
    password: str
    email: str

    @field_validator('password')
    @classmethod
    def password_hash(cls, v):
        if v is not None:
            return get_password_hash(v)


class GetUserSchema(BaseUserSchema):
    id: int
    username: str
    email: str
    created_at: datetime.datetime


class SearchUserSchema(BaseUserSchema):
    id: int | None = None
    username: str | None = None
    email: str | None = None


class UpdateUserSchema(BaseUserSchema):
    username: str | None = None


class DeleteUserSchema(SearchUserSchema):
    pass


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


class LoginSchema(BaseModel):
    email: str
    password: str


class DefaultUserResponse(DefaultResponse):
    data: list | dict | None = None


class GetUserResponse(DefaultUserResponse):
    data: GetUserSchema


class GetManyUsersResponse(DefaultUserResponse):
    data: list[GetUserSchema]


class LoginResponse(DefaultResponse):
    access_token: str
