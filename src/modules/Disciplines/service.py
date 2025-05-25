from modules.Disciplines.repository import DisciplineRepo
from modules.Disciplines.schemas import (
    CreateDisciplineSchema, SearchDisciplineSchema,
    UpdateDisciplineSchema, DeleteDisciplineSchema, GetDisciplineSchema
)


class DisciplineService:
    def __init__(self, discipline_repo: DisciplineRepo):
        self._repo = discipline_repo

    async def create(self, data: CreateDisciplineSchema) -> GetDisciplineSchema:
        discipline = await self._repo.create_one(data.model_dump(exclude_none=True))
        return discipline

    async def get_one(self, data: SearchDisciplineSchema) -> GetDisciplineSchema:
        discipline = await self._repo.get_one(data.model_dump(exclude_none=True))
        return discipline

    async def get_many(self, data: SearchDisciplineSchema) -> list[GetDisciplineSchema]:
        disciplines = await self._repo.get_many(data.model_dump(exclude_none=True))
        return disciplines

    async def update_by_id(self, discipline_id: int, data: UpdateDisciplineSchema) -> GetDisciplineSchema:
        discipline = await self._repo.update_by_id(discipline_id, data.model_dump(exclude_none=True))
        return discipline

    async def delete_one(self, data: DeleteDisciplineSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteDisciplineSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
