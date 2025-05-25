from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped

from models.base import Base
from models.professor_discipline import professor_discipline
from modules.Disciplines.schemas import GetDisciplineSchema


class Disciplines(Base):
    __tablename__ = 'disciplines'
    __mapper_args__ = {
        'polymorphic_identity': 'discipline',
    }

    id = Column(Integer, primary_key=True, index=True)
    discipline_name = Column(String(50), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    has_practice = Column(Boolean, default=True)
    has_labs = Column(Boolean, default=True)
    authors = Column(String(100), nullable=False)

    professors: Mapped[list['Professor']] = relationship(
        secondary=professor_discipline,
        back_populates='disciplines',
        lazy='selectin'
    )

    def to_read_model(self) -> "GetDisciplineSchema":
        return GetDisciplineSchema(
            id=self.id,
            discipline_name=self.discipline_name,
            description=self.description,
            has_practice=self.has_practice,
            has_labs=self.has_labs,
            authors=self.authors
        )

from .professor import Professor
