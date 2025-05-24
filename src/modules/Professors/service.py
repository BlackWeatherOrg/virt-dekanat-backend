from modules.Professors.repository import ProfessorRepo
from modules.Professors.schemas import (
    CreateProfessorSchema, SearchProfessorSchema,
    UpdateProfessorSchema, DeleteProfessorSchema, GetProfessorSchema
)


class ProfessorService:
    def __init__(self, professor_repo: ProfessorRepo):
        self._repo = professor_repo

    async def create(self, data: CreateProfessorSchema) -> GetProfessorSchema:
        prof = await self._repo.create_one(data.model_dump(exclude_none=True))
        return prof

    async def get_one(self, data: SearchProfessorSchema) -> GetProfessorSchema:
        prof = await self._repo.get_one(data.model_dump(exclude_none=True))
        return prof

    async def get_many(self, data: SearchProfessorSchema) -> list[GetProfessorSchema]:
        profs = await self._repo.get_many(data.model_dump(exclude_none=True))
        return profs

    async def update_by_id(self, professor_id: int, data: UpdateProfessorSchema) -> GetProfessorSchema:
        prof = await self._repo.update_by_id(professor_id, data.model_dump(exclude_none=True))
        return prof

    async def delete_one(self, data: DeleteProfessorSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteProfessorSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
