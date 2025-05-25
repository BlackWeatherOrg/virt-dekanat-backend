from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from db.helpers import async_session_maker
from models.user import User
from utils.base_repository import SQLAlchemyRepository
from utils.exceptions import ObjectDoesNotExistException


class UserRepo(SQLAlchemyRepository):
    model = User

    async def get_password(self, username: str) -> str:
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(username=username)
            try:
                res = await session.execute(stmt)
                return res.scalar_one().password
            except NoResultFound as e:
                raise ObjectDoesNotExistException from e
