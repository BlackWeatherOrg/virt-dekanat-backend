from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

from db.helpers import async_session_maker
from utils.base_repository import SQLAlchemyRepository
from models.grade import Grades
from utils.exceptions import IntegrityException


class GradeRepo(SQLAlchemyRepository):
    model = Grades

    async def create_one(self, data: dict):
        async with async_session_maker() as session:
            try:
                grade = Grades(**data)
                session.add(grade)
                await session.commit()
                await session.refresh(grade)
                return grade.to_read_model()
            except IntegrityError as e:
                raise IntegrityException from e
