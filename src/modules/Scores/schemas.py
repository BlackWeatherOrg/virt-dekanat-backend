import datetime
from pydantic import BaseModel, Field

from utils.base_schema import DefaultResponse


class BaseScoreSchema(BaseModel):
    value: int = Field(..., ge=0, le=54)
    issued_date: datetime.date


class CreateScoreSchema(BaseScoreSchema):
    user_id: int  # ID пользователя, которому выставляется оценка


class GetScoreSchema(BaseScoreSchema):
    id: int
    created_at: datetime.datetime


class SearchScoreSchema(BaseModel):
    id: int | None = None
    user_id: int | None = None
    value: int | None = None
    issued_date: datetime.date | None = None


class UpdateScoreSchema(BaseModel):
    id: int
    value: int | None = Field(None, ge=0, le=54)
    issued_date: datetime.date | None = None


class DeleteScoreSchema(BaseModel):
    id: int


class DefaultScoreResponse(DefaultResponse):
    data: list | dict | None = None


class GetScoreResponse(DefaultScoreResponse):
    data: GetScoreSchema


class GetManyScoresResponse(DefaultScoreResponse):
    data: list[GetScoreSchema]
