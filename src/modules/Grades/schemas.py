import datetime
from pydantic import BaseModel, Field

from modules.Disciplines.schemas import GetDisciplineSchema
from modules.Professors.schemas import GetProfessorSchema
from modules.Student.schemas import GetStudentSchema
from utils.base_schema import DefaultResponse


class BaseGradeSchema(BaseModel):
    value: int = Field(..., ge=0, le=54)


class CreateGradeSchema(BaseGradeSchema):
    student_id: int
    professor_id: int
    discipline_id: int


class GetGradeSchema(BaseGradeSchema):
    id: int
    student: GetStudentSchema
    professor: GetProfessorSchema
    discipline: GetDisciplineSchema
    created_at: datetime.datetime


class SearchGradeSchema(BaseModel):
    id: int | None = None
    user_id: int | None = None
    value: int | None = None
    student_id: int | None = None
    professor_id: int | None = None
    discipline_id: int | None = None


class UpdateGradeSchema(BaseModel):
    id: int
    value: int | None = Field(None, ge=0, le=54)


class DeleteGradeSchema(BaseModel):
    id: int


class DefaultGradeResponse(DefaultResponse):
    data: list | dict | None = None


class GetGradeResponse(DefaultGradeResponse):
    data: GetGradeSchema


class GetManyGradesResponse(DefaultGradeResponse):
    data: list[GetGradeSchema]
