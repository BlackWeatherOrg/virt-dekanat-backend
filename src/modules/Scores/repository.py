from utils.base_repository import SQLAlchemyRepository
from models.score import Score


class ScoreRepo(SQLAlchemyRepository):
    model = Score