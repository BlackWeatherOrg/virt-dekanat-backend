from sqlalchemy.exc import IntegrityError

from db.helpers import async_session_maker
from utils.base_repository import SQLAlchemyRepository
from models.professor import Professor
from utils.exceptions import IntegrityException


class ProfessorRepo(SQLAlchemyRepository):
    model = Professor

    async def create_one(self, data: dict):
        async with async_session_maker() as session:
            try:
                data['role_id'] = 3
                professor = Professor(**data)
                session.add(professor)
                await session.commit()
                return professor.to_read_model()
            except IntegrityError as e:
                raise IntegrityException from e
