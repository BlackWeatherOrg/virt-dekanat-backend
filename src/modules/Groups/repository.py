
from models.group import Groups
from utils.base_repository import SQLAlchemyRepository


class GroupRepo(SQLAlchemyRepository):
    model = Groups
