from models.discipline import Disciplines
from utils.base_repository import SQLAlchemyRepository


class DisciplineRepo(SQLAlchemyRepository):
    model = Disciplines
