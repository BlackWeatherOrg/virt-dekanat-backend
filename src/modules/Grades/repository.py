from utils.base_repository import SQLAlchemyRepository
from models.grade import Grades


class GradeRepo(SQLAlchemyRepository):
    model = Grades
