from modules.Groups.repository import GroupRepo
from modules.Groups.schemas import (
    CreateGroupSchema, SearchGroupSchema,
    UpdateGroupSchema, DeleteGroupSchema, GetGroupSchema
)


class GroupService:
    def __init__(self, group_repo: GroupRepo):
        self._repo = group_repo

    async def create(self, data: CreateGroupSchema) -> GetGroupSchema:
        group = await self._repo.create_one(data.model_dump(exclude_none=True))
        return group

    async def get_one(self, data: SearchGroupSchema) -> GetGroupSchema:
        group = await self._repo.get_one(data.model_dump(exclude_none=True))
        return group

    async def get_many(self, data: SearchGroupSchema) -> list[GetGroupSchema]:
        groups = await self._repo.get_many(data.model_dump(exclude_none=True))
        return groups

    async def update_by_id(self, group_id: int, data: UpdateGroupSchema) -> GetGroupSchema:
        group = await self._repo.update_by_id(group_id, data.model_dump(exclude_none=True))
        return group

    async def delete_one(self, data: DeleteGroupSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteGroupSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
