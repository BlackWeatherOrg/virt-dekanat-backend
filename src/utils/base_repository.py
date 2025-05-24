from abc import ABC, abstractmethod

from sqlalchemy import delete, desc, insert, select, update
from sqlalchemy.exc import (IntegrityError, MultipleResultsFound,
                            NoResultFound, ProgrammingError)

from db.helpers import async_session_maker
from utils.exceptions import (IntegrityException,
                              MultipleResultsFoundException,
                              ObjectDoesNotExistException,
                              ProgrammingException)


class AbstractRepository(ABC):
    """
    Абстрактный класс репозитория для CRUD операций
    """
    @abstractmethod
    async def create_one(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_many(self, *args, **kwargs):
        pass

    @abstractmethod
    async def update_by_id(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete_one(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete_many(self, *args, **kwargs):
        pass


class SQLAlchemyRepository(AbstractRepository):
    """
    Базовый класс репозитория для взаимодействия с бд
    """

    model = None

    async def create_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            try:
                res = await session.execute(stmt)
                await session.commit()
                return res.scalar_one().to_read_model()
            except IntegrityError as e:
                raise IntegrityException from e

    async def get_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**data)
            try:
                res = await session.execute(stmt)
                return res.scalars().one().to_read_model()
            except NoResultFound as e:
                raise ObjectDoesNotExistException from e
            except MultipleResultsFound as e:
                raise MultipleResultsFoundException from e

    async def get_many(self, data: dict, order_by=None, descending_order: bool = False) -> list:
        async with async_session_maker() as session:
            if descending_order:
                stmt = select(self.model).filter_by(**data).order_by(desc(order_by))
            else:
                stmt = select(self.model).filter_by(**data).order_by(order_by)
            res = await session.execute(stmt)
            return [row[0].to_read_model() for row in res.all()]

    async def update_by_id(self, item_id: int, data: dict):
        async with async_session_maker() as session:
            stmt = update(self.model).values(
                **data).filter_by(id=item_id).returning(self.model)
            try:
                res = await session.execute(stmt)
                await session.commit()

                return res.scalar_one().to_read_model()
            except NoResultFound as e:
                raise ObjectDoesNotExistException from e
            except IntegrityError as e:
                raise IntegrityException from e
            except ProgrammingError as e:
                raise ProgrammingException from e

    async def delete_one(self, data: dict) -> None:
        pass
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**data)
            try:
                res = await session.execute(stmt)
                await session.delete(res.scalars().one())
                await session.commit()
            except MultipleResultsFound as e:
                raise MultipleResultsFoundException from e

    async def delete_many(self, data: dict) -> None:
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(**data)
            await session.execute(stmt)
            await session.commit()
