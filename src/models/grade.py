import datetime

from sqlalchemy import Column, Integer, Date, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SqlEnum

from models.base import Base
from modules.Grades.schemas import GetGradeSchema
from utils.enums.grades import GradeEnum


class Grades(Base):
    __tablename__ = 'grades'
    __mapper_args__ = {
        'polymorphic_identity': 'grade',
        'eager_defaults': True
    }

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False)
    type: Mapped[GradeEnum] = mapped_column(SqlEnum(GradeEnum), default='MODULE1', server_default='MODULE1')
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
            type=self.type,
            student=self.student.to_read_model(),
            professor=self.professor.to_read_model(),
            discipline=self.discipline.to_read_model(),
            created_at=self.created_at
        )

from .discipline import Disciplines
from .professor import Professor
from .student import Student
