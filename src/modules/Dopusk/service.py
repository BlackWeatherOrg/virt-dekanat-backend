from modules.Dopusk.repository import DopuskRepo
from modules.Dopusk.schemas import (
    CreateDopuskSchema, SearchDopuskSchema,
    UpdateDopuskSchema, DeleteDopuskSchema, GetDopuskSchema
)


class DopuskService:
    def __init__(self, dopusk_repo: DopuskRepo):
        self._repo = dopusk_repo

    async def create(self, data: dict) -> GetDopuskSchema:
        dopusk = await self._repo.create_one(data)
        return dopusk

    async def get_one(self, data: SearchDopuskSchema) -> GetDopuskSchema:
        dopusk = await self._repo.get_one(data.model_dump(exclude_none=True))
        return dopusk

    async def get_many(self, data: SearchDopuskSchema) -> list[GetDopuskSchema]:
        dopusks = await self._repo.get_many(data.model_dump(exclude_none=True))
        return dopusks

    async def update_by_id(self, dopusk_id: int, data: UpdateDopuskSchema) -> GetDopuskSchema:
        dopusk = await self._repo.update_by_id(dopusk_id, data.model_dump(exclude_none=True))
        return dopusk

    async def delete_one(self, data: DeleteDopuskSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteDopuskSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
