import datetime
from pydantic import BaseModel, Field, EmailStr


class BaseProfessorSchema(BaseModel):
    passport_number: str = Field(..., max_length=20)
    first_name: str
    middle_name: str | None = None
    last_name: str
    teaching_experience: int = Field(..., ge=0)
    academic_degree: str | None = None
    department: str | None = None
    email: EmailStr
    phone_number: str | None = None


class CreateProfessorSchema(BaseProfessorSchema):
    pass


class GetProfessorSchema(BaseProfessorSchema):
    id: int
    created_at: datetime.datetime


class SearchProfessorSchema(BaseModel):
    id: int | None = None
    passport_number: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    academic_degree: str | None = None
    department: str | None = None
    email: EmailStr | None = None


class UpdateProfessorSchema(BaseModel):
    id: int
    passport_number: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    teaching_experience: int | None = None
    academic_degree: str | None = None
    department: str | None = None
    email: EmailStr | None = None
    phone_number: str | None = None


class DeleteProfessorSchema(BaseModel):
    id: int


class DefaultProfessorResponse(BaseModel):
    message: str


class GetProfessorResponse(DefaultProfessorResponse):
    data: GetProfessorSchema


class GetManyProfessorsResponse(DefaultProfessorResponse):
    data: list[GetProfessorSchema]
