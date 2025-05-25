import datetime

from sqlalchemy import Column, Integer, Date, func
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from modules.Grades.schemas import GetGradeSchema


class Grades(Base):
    __tablename__ = 'grades'
    __mapper_args__ = {
        'polymorphic_identity': 'grade',
    }

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False)
    issued_date = Column(Date, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def to_read_model(self) -> "GetGradeSchema":
        return GetGradeSchema(
            id=self.id,
            value=self.value,
            issued_date=self.issued_date,
            created_at=self.created_at
        )
