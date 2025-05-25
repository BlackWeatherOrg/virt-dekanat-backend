import datetime

from sqlalchemy import Column, Integer, Date, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base
from modules.Grades.schemas import GetGradeSchema


class Grades(Base):
    __tablename__ = 'grades'
    __mapper_args__ = {
        'polymorphic_identity': 'grade',
    }

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False)
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

    def to_read_model(self) -> "GetGradeSchema":
        return GetGradeSchema(
            id=self.id,
            value=self.value,
            student=self.student.to_read_model(),
            professor=self.professor.to_read_model(),
            discipline=self.discipline.to_read_model(),
            created_at=self.created_at
        )

from .discipline import Disciplines
from .professor import Professor
from .student import Student
