import datetime

from sqlalchemy import Column, Integer, Date, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SqlEnum

from models.base import Base
from modules.Dopusk.schemas import GetDopuskSchema
from utils.enums.grades import GradeEnum


class Dopusk(Base):
    __tablename__ = 'dopuski'
    __mapper_args__ = {
        'polymorphic_identity': 'dopusk',
        'eager_defaults': True
    }

    id = Column(Integer, primary_key=True, index=True)
    type: Mapped[GradeEnum] = mapped_column(SqlEnum(GradeEnum), default='MODULE1', server_default='MODULE1')
    date: Mapped[datetime.date]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    student_id: Mapped[int] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    student: Mapped['Student'] = relationship(
        lazy='joined'
    )

    professor_id: Mapped[int] = mapped_column(ForeignKey('professors.id', ondelete='CASCADE'))
    professor: Mapped['Professor'] = relationship(
        lazy='joined'
    )

    discipline_id: Mapped[int] = mapped_column(ForeignKey('disciplines.id', ondelete='CASCADE'))
    discipline: Mapped['Disciplines'] = relationship(
        lazy='joined'
    )

    def to_read_model(self) -> "GetDopuskSchema":
        return GetDopuskSchema(
            id=self.id,
            type=self.type,
            date=self.date,
            student=self.student.to_read_model(),
            professor=self.professor.to_read_model(),
            discipline=self.discipline.to_read_model(),
            created_at=self.created_at
        )

from .discipline import Disciplines
from .professor import Professor
from .student import Student
