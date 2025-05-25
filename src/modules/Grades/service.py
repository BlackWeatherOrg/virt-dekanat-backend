from modules.Grades.repository import GradeRepo
from modules.Grades.schemas import (
    CreateGradeSchema, SearchGradeSchema,
    UpdateGradeSchema, DeleteGradeSchema, GetGradeSchema
)


class GradeService:
    def __init__(self, grade_repo: GradeRepo):
        self._repo = grade_repo

    async def create(self, data: CreateGradeSchema) -> GetGradeSchema:
        grade = await self._repo.create_one(data.model_dump(exclude_none=True))
        return grade

    async def get_one(self, data: SearchGradeSchema) -> GetGradeSchema:
        grade = await self._repo.get_one(data.model_dump(exclude_none=True))
        return grade

    async def get_many(self, data: SearchGradeSchema) -> list[GetGradeSchema]:
        grades = await self._repo.get_many(data.model_dump(exclude_none=True))
        return grades

    async def update_by_id(self, grade_id: int, data: UpdateGradeSchema) -> GetGradeSchema:
        grade = await self._repo.update_by_id(grade_id, data.model_dump(exclude_none=True))
        return grade

    async def delete_one(self, data: DeleteGradeSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteGradeSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
