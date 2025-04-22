import bcrypt
from utils.enums.user import PermissionsEnum
from sqlalchemy import (
    Column, Integer, String, Table, ForeignKey
)
from sqlalchemy.orm import relationship

from models.base import Base


user_roles = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

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
    password_hash = Column(String(128), nullable=False)

    roles = relationship(
        "Role",
        secondary="user_roles",
        back_populates="users"
    )

    def set_password(self, password: str) -> None:
        self.password_hash = bcrypt.hash(password)

    def check_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship(
        "User",
        secondary=user_roles,
        back_populates="roles"
    )
    permissions = relationship(
        "Permission",
        secondary=role_permissions,
        back_populates="roles"
    )


class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    roles = relationship(
        "Role",
        secondary=role_permissions,
        back_populates="permissions"
    )
