import datetime
from pydantic import BaseModel, Field, EmailStr, field_validator

from utils.base_schema import DefaultResponse
from utils.password_utils import get_password_hash


class BaseProfessorSchema(BaseModel):
    first_name: str
    username: str
    middle_name: str | None = None
    last_name: str
    teaching_experience: int = Field(..., ge=0)
    academic_degree: str | None = None
    email: EmailStr
    phone_number: str | None = None


class CreateProfessorSchema(BaseProfessorSchema):
    password: str

    @field_validator('password')
    @classmethod
    def password_hash(cls, v):
        if v is not None:
            return get_password_hash(v)


class GetProfessorSchema(BaseProfessorSchema):
    id: int
    created_at: datetime.datetime


class SearchProfessorSchema(BaseModel):
    id: int | None = None
    username: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    academic_degree: str | None = None
    email: EmailStr | None = None


class UpdateProfessorSchema(BaseModel):
    id: int
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    teaching_experience: int | None = None
    academic_degree: str | None = None
    email: EmailStr | None = None
    phone_number: str | None = None


class DeleteProfessorSchema(BaseModel):
    id: int


class DefaultProfessorResponse(DefaultResponse):
    data: list | dict | None = None


class GetProfessorResponse(DefaultProfessorResponse):
    data: GetProfessorSchema


class GetManyProfessorsResponse(DefaultProfessorResponse):
    data: list[GetProfessorSchema]
