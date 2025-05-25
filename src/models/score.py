from sqlalchemy import Column, Integer, Date, ForeignKey
from models import User
from modules.Scores.schemas import GetScoreSchema


class Score(User):
    __tablename__ = 'scores'
    __mapper_args__ = {
        'polymorphic_identity': 'score',
    }

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    value = Column(Integer, nullable=False)
    issued_date = Column(Date, nullable=False)

    def to_read_model(self) -> "GetScoreSchema":
        return GetScoreSchema(
            id=self.id,
            value=self.value,
            issued_date=self.issued_date,
            created_at=self.created_at
        )
