from sqlalchemy import insert, update
from sqlalchemy.exc import IntegrityError, NoResultFound, ProgrammingError

from db.helpers import async_session_maker
from utils.base_repository import SQLAlchemyRepository
from models.grade import Grades
from utils.exceptions import IntegrityException, ObjectDoesNotExistException, ProgrammingException


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

    async def update_by_id(self, item_id: int, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).values(
                **data).filter_by(id=item_id).returning(self.model)
            try:
                res = await session.execute(stmt)
                await session.commit()

                updated_item = res.scalar_one()
                await session.refresh(updated_item)

                return updated_item.to_read_model()
            except NoResultFound as e:
                raise ObjectDoesNotExistException from e
            except IntegrityError as e:
                raise IntegrityException from e
            except ProgrammingError as e:
                raise ProgrammingException from e
