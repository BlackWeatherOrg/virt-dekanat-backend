from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import User
from modules.Student.schemas import GetStudentSchema


class Student(User):
    __tablename__ = 'students'
    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group_id: Mapped[str] = mapped_column(ForeignKey('groups.id', ondelete='CASCADE'))
    group: Mapped['Groups'] = relationship(
        back_populates='students',
        lazy='joined'
    )

    def to_read_model(self) -> GetStudentSchema:
        return GetStudentSchema(
            id=self.id,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
            email=self.email,
            group=self.group.to_read_model(),
            created_at=self.created_at,
            role=self.role.to_read_model()
        )


from .group import Groups
