import datetime
from pydantic import BaseModel, Field

from modules.Disciplines.schemas import GetDisciplineSchema
from modules.Professors.schemas import GetProfessorSchema
from modules.Student.schemas import GetStudentSchema
from utils.base_schema import DefaultResponse
from utils.enums.grades import GradeEnum


class CreateDopuskSchema(BaseModel):
    professor_id: int
    date: datetime.date
    type: GradeEnum
    discipline_id: int


class GetDopuskSchema(BaseModel):
    id: int
    type: GradeEnum
    student: GetStudentSchema
    professor: GetProfessorSchema
    discipline: GetDisciplineSchema
    created_at: datetime.datetime


class SearchDopuskSchema(BaseModel):
    id: int | None = None
    value: int | None = None
    type: GradeEnum | None = None
    student_id: int | None = None
    professor_id: int | None = None
    discipline_id: int | None = None


class UpdateDopuskSchema(BaseModel):
    id: int
    value: int | None = Field(None, ge=0, le=54)


class DeleteDopuskSchema(BaseModel):
    id: int


class DefaultDopuskResponse(DefaultResponse):
    data: list | dict | None = None


class GetDopuskResponse(DefaultDopuskResponse):
    data: GetDopuskSchema


class GetManyDopusksResponse(DefaultDopuskResponse):
    data: list[GetDopuskSchema]
