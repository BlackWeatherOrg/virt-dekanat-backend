from modules.Scores.repository import ScoreRepo
from modules.Scores.schemas import (
    CreateScoreSchema, SearchScoreSchema,
    UpdateScoreSchema, DeleteScoreSchema, GetScoreSchema
)


class ScoreService:
    def __init__(self, score_repo: ScoreRepo):
        self._repo = score_repo

    async def create(self, data: CreateScoreSchema) -> GetScoreSchema:
        score = await self._repo.create_one(data.model_dump(exclude_none=True))
        return score

    async def get_one(self, data: SearchScoreSchema) -> GetScoreSchema:
        score = await self._repo.get_one(data.model_dump(exclude_none=True))
        return score

    async def get_many(self, data: SearchScoreSchema) -> list[GetScoreSchema]:
        scores = await self._repo.get_many(data.model_dump(exclude_none=True))
        return scores

    async def update_by_id(self, score_id: int, data: UpdateScoreSchema) -> GetScoreSchema:
        score = await self._repo.update_by_id(score_id, data.model_dump(exclude_none=True))
        return score

    async def delete_one(self, data: DeleteScoreSchema) -> None:
        await self._repo.delete_one(data.model_dump(exclude_none=True))

    async def delete_many(self, data: DeleteScoreSchema) -> None:
        await self._repo.delete_many(data.model_dump(exclude_none=True))
