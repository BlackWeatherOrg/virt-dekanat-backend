from sqlalchemy.exc import IntegrityError

from db.helpers import async_session_maker
from utils.base_repository import SQLAlchemyRepository
from models.dopusk import Dopusk
from utils.exceptions import IntegrityException


class DopuskRepo(SQLAlchemyRepository):
    model = Dopusk

    async def create_one(self, data: dict):
        async with async_session_maker() as session:
            try:
                dopusk = Dopusk(**data)
                session.add(dopusk)
                await session.commit()
                await session.refresh(dopusk)
                return dopusk.to_read_model()
            except IntegrityError as e:
                raise IntegrityException from e
