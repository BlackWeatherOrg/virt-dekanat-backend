import datetime

from pydantic import BaseModel, field_validator

from modules.Groups.schemas import GetGroupSchema
from modules.Users.schemas import GetRoleSchema
from utils.base_schema import DefaultResponse
from utils.password_utils import get_password_hash


class BaseStudentSchema(BaseModel):
    username: str


class CreateStudentSchema(BaseStudentSchema):
    password: str
    email: str
    first_name: str
    last_name: str
    group_id: str
    middle_name: str | None = None


    @field_validator('password')
    @classmethod
    def password_hash(cls, v):
        if v is not None:
            return get_password_hash(v)


class GetStudentSchema(BaseStudentSchema):
    id: int
    username: str
    first_name: str
    last_name: str
    middle_name: str | None = None
    group: GetGroupSchema
    email: str
    created_at: datetime.datetime
    role: GetRoleSchema


class SearchStudentSchema(BaseStudentSchema):
    id: int | None = None
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    group_id: str | None = None
    role_id: int | None = None
    email: str | None = None


class UpdateStudentSchema(BaseStudentSchema):
    group_id: str | None = None


class DeleteStudentSchema(SearchStudentSchema):
    pass


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class DefaultStudentResponse(DefaultResponse):
    data: list | dict | None = None


class GetStudentResponse(DefaultStudentResponse):
    data: GetStudentSchema


class GetManyStudentsResponse(DefaultStudentResponse):
    data: list[GetStudentSchema]


class LoginResponse(DefaultResponse):
    access_token: str

