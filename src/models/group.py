from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from models.base import Base
from modules.Groups.schemas import GetGroupSchema


class Groups(Base):
    __tablename__ = 'groups'
    __mapper_args__ = {
        'polymorphic_identity': 'group',
    }

    id = Column(String(30), primary_key=True, index=True)
    institute = Column(String(100), nullable=False)
    orientation = Column(String(500), nullable=False)

    students: Mapped[list['Student']] = relationship(
        back_populates='group',
        lazy='selectin'
    )

    def to_read_model(self) -> "GetGroupSchema":
        return GetGroupSchema(
            id=self.id,
            institute=self.institute,
            orientation=self.orientation,
        )

from .student import Student



