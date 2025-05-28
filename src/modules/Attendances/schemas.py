import datetime
from pydantic import BaseModel

from modules.Disciplines.schemas import GetDisciplineSchema
from modules.Student.schemas import GetStudentSchema
from utils.base_schema import DefaultResponse


class CreateAttendanceSchema(BaseModel):
    student_id: int
    discipline_id: int
    date: datetime.date
    visited: bool


class GetAttendanceSchema(BaseModel):
    id: int
    visited: bool
    date: datetime.date
    student: GetStudentSchema
    discipline: GetDisciplineSchema
    created_at: datetime.datetime


class SearchAttendanceSchema(BaseModel):
    id: int | None = None
    visited: bool | None = None
    date: datetime.date | None = None
    student_id: int | None = None
    discipline_id: int | None = None


class UpdateAttendanceSchema(BaseModel):
    id: int
    visited: bool | None = None


class DeleteAttendanceSchema(BaseModel):
    id: int


class DefaultAttendanceResponse(DefaultResponse):
    data: list | dict | None = None


class GetAttendanceResponse(DefaultAttendanceResponse):
    data: GetAttendanceSchema


class GetManyAttendancesResponse(DefaultAttendanceResponse):
    data: list[GetAttendanceSchema]
