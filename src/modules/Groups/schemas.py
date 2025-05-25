from pydantic import BaseModel

from utils.base_schema import DefaultResponse


class CreateGroupSchema(BaseModel):
    id: str = 'ИДБ-22-10'
    institute: str
    orientation: str


class GetGroupSchema(BaseModel):
    id: str
    institute: str
    orientation: str


class SearchGroupSchema(BaseModel):
    id: str | None = None
    institute: str | None = None
    orientation: str | None = None


class UpdateGroupSchema(BaseModel):
    id: str
    institute: str | None = None
    orientation: str | None = None


class DeleteGroupSchema(BaseModel):
    id: str

class DefaultGroupResponse(DefaultResponse):
    data: list | dict | None = None


class GetGroupResponse(DefaultGroupResponse):
    data: GetGroupSchema


class GetManyGroupsResponse(DefaultGroupResponse):
    data: list[GetGroupSchema]

