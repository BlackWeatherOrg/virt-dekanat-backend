from sqlalchemy.exc import IntegrityError

from db.helpers import async_session_maker
from models.student import Student
from utils.base_repository import SQLAlchemyRepository
from utils.exceptions import IntegrityException


class StudentRepo(SQLAlchemyRepository):
    model = Student

    async def create_one(self, data: dict):
        async with async_session_maker() as session:
            try:
                data['role_id'] = 1
                student = Student(**data)
                session.add(student)
                await session.commit()
                await session.refresh(student)
                return student.to_read_model()
            except IntegrityError as e:
                raise IntegrityException from e
