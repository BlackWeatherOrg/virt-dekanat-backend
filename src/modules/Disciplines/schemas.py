from pydantic import BaseModel

from utils.base_schema import DefaultResponse


class CreateDisciplineSchema(BaseModel):
    discipline_name: str
    description: str
    has_practice: bool
    has_labs: bool
    authors: str


class GetDisciplineSchema(BaseModel):
    id: int
    discipline_name: str
    description: str
    has_practice: bool
    has_labs: bool
    authors: str

class SearchDisciplineSchema(BaseModel):
    id: int | None = None
    discipline_name: str | None = None
    description: str | None = None
    has_practice: bool | None = None
    has_labs: bool | None = None
    authors: str | None = None


class UpdateDisciplineSchema(BaseModel):
    id: int
    discipline_name: str | None = None
    description: str | None = None
    has_practice: bool | None = None
    has_labs: bool | None = None
    authors: str | None = None


class DeleteDisciplineSchema(BaseModel):
    id: int


class DefaultDisciplineResponse(DefaultResponse):
    data: list | dict | None = None


class GetDisciplineResponse(DefaultDisciplineResponse):
    data: GetDisciplineSchema


class GetManyDisciplinesResponse(DefaultDisciplineResponse):
    data: list[GetDisciplineSchema]

