import datetime

from modules.Users.schemas import GetUserSchema, GetRoleSchema, GetPermissionSchema
from utils.enums.user import PermissionsEnum, DatabasesEnum
from sqlalchemy import (
    Column, Integer, String, Table, ForeignKey, func
)
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import Enum as SqlEnum

from models.base import Base


role_permissions = Table(
    'role_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    middle_name = Column(String(50))
    password = Column(String(128), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), default=1, unique=False)

    role: Mapped['Role'] = relationship(
        back_populates="users",
        lazy='selectin'
    )

    def to_read_model(self) -> GetUserSchema:
        return GetUserSchema(
            id=self.id,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name,
            email=self.email,
            created_at=self.created_at,
            role=self.role.to_read_model()
        )



class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    users: Mapped[list['User']] = relationship(
        back_populates="role",
        lazy="selectin"
    )
    permissions: Mapped[list['Permission']] = relationship(
        secondary=role_permissions,
        lazy='selectin'
    )

    def to_read_model(self) -> GetRoleSchema:
        return GetRoleSchema(
            id=self.id,
            name=self.name,
            permissions=[perm.to_read_model() for perm in self.permissions]
        )


class Permission(Base):
    __tablename__ = 'permissions'
    __mapper_args__ = {'eager_defaults': True}

    id = Column(Integer, primary_key=True, index=True)
    database: Mapped[DatabasesEnum] = mapped_column(SqlEnum(DatabasesEnum))
    permission_type: Mapped[PermissionsEnum] = mapped_column(SqlEnum(PermissionsEnum), default=PermissionsEnum.READ)

    def to_read_model(self) -> GetPermissionSchema:
        return GetPermissionSchema(
            id=self.id,
            database=self.database,
            permission=self.permission_type
        )
