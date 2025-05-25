import datetime
from pydantic import BaseModel, Field

from utils.base_schema import DefaultResponse


class BaseGradeSchema(BaseModel):
    value: int = Field(..., ge=0, le=54)
    issued_date: datetime.date


class CreateGradeSchema(BaseGradeSchema):
    pass


class GetGradeSchema(BaseGradeSchema):
    id: int
    created_at: datetime.datetime


class SearchGradeSchema(BaseModel):
    id: int | None = None
    user_id: int | None = None
    value: int | None = None
    issued_date: datetime.date | None = None


class UpdateGradeSchema(BaseModel):
    id: int
    value: int | None = Field(None, ge=0, le=54)
    issued_date: datetime.date | None = None


class DeleteGradeSchema(BaseModel):
    id: int


class DefaultGradeResponse(DefaultResponse):
    data: list | dict | None = None


class GetGradeResponse(DefaultGradeResponse):
    data: GetGradeSchema


class GetManyGradesResponse(DefaultGradeResponse):
    data: list[GetGradeSchema]
