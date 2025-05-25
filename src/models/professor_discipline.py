from sqlalchemy import ForeignKey, Column, Table

from models.base import Base

professor_discipline = Table(
    'professor_disciplines',
    Base.metadata,
    Column('professor_id', ForeignKey('professors.id'), primary_key=True),
    Column('discipline_id', ForeignKey('disciplines.id'), primary_key=True)
)
