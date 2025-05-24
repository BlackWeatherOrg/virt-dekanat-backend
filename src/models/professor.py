from sqlalchemy import Column, Integer, String, ForeignKey
from models.user import User
from modules.Professors.schemas import GetProfessorSchema


class Professor(User):
    __tablename__ = 'professors'
    __mapper_args__ = {
        'polymorphic_identity': 'professor',
    }

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    passport_number = Column(String(20), unique=True, nullable=False)
    teaching_experience = Column(Integer, nullable=False, default=0)
    academic_degree = Column(String(100), nullable=True)
    phone_number = Column(String(20), nullable=True)

    def to_read_model(self) -> "GetProfessorSchema":
        from modules.Professors.schemas import GetProfessorSchema
        return GetProfessorSchema(
            id=self.id,
            passport_number=self.passport_number,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            teaching_experience=self.teaching_experience,
            academic_degree=self.academic_degree,
            department=self.department,
            email=self.email,
            phone_number=self.phone_number,
            created_at=self.created_at
        )
