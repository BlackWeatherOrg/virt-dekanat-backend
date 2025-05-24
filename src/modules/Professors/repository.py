from utils.base_repository import SQLAlchemyRepository
from models.professor import Professor


class ProfessorRepo(SQLAlchemyRepository):
    model = Professor
