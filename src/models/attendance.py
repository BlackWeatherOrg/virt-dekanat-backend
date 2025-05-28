import datetime

from sqlalchemy import Column, Integer, func, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from modules.Attendances.schemas import GetAttendanceSchema


class Attendances(Base):
    __tablename__ = 'attendances'
    __mapper_args__ = {
        'polymorphic_identity': 'attendance',
        'eager_defaults': True
    }

    id = Column(Integer, primary_key=True, index=True)
    visited = Column(Boolean)
    date: Mapped[datetime.date]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    student_id: Mapped[int] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    student: Mapped['Student'] = relationship(
        lazy='joined'
    )

    discipline_id: Mapped[int] = mapped_column(ForeignKey('disciplines.id', ondelete='CASCADE'))
    discipline: Mapped['Disciplines'] = relationship(
        lazy='joined'
    )

    def to_read_model(self) -> "GetAttendanceSchema":
        return GetAttendanceSchema(
            id=self.id,
            visited=self.visited,
            date=self.date,
            student=self.student.to_read_model(),
            discipline=self.discipline.to_read_model(),
            created_at=self.created_at
        )

from .discipline import Disciplines
from .student import Student
