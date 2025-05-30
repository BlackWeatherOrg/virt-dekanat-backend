import datetime

from pydantic import BaseModel, field_validator

from utils.base_schema import DefaultResponse
from utils.password_utils import get_password_hash


class BaseUserSchema(BaseModel):
    username: str


class CreateUserSchema(BaseUserSchema):
    password: str
    email: str
    first_name: str
    last_name: str
    middle_name: str | None = None


    @field_validator('password')
    @classmethod
    def password_hash(cls, v):
        if v is not None:
            return get_password_hash(v)


class GetPermissionSchema(BaseModel):
    id: int
    database: str
    permission: str


class GetRoleSchema(BaseModel):
    id: int
    name: str
    permissions: list[GetPermissionSchema]


class GetUserSchema(BaseUserSchema):
    id: int
    username: str
    first_name: str
    last_name: str
    middle_name: str | None = None
    email: str
    created_at: datetime.datetime
    role: GetRoleSchema


class SearchUserSchema(BaseUserSchema):
    id: int | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    role_id: int | None = None
    email: str | None = None


class UpdateUserSchema(BaseUserSchema):
    username: str | None = None


class DeleteUserSchema(SearchUserSchema):
    pass


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class DefaultUserResponse(DefaultResponse):
    data: list | dict | None = None


class GetUserResponse(DefaultUserResponse):
    data: GetUserSchema


class GetManyUsersResponse(DefaultUserResponse):
    data: list[GetUserSchema]


class LoginResponse(DefaultResponse):
    access_token: str

