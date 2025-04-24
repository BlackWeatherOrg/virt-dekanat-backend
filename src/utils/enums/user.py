from enum import Enum


class PermissionsEnum(str, Enum):
    READ = 'read'
    UPDATE = 'update'
    DELETE = 'delete'
    CREATE = 'create'


class DatabasesEnum(str, Enum):
    ROLES = 'roles'
    DISCIPLINES = 'disciplines'
    USERS = 'users'
    GRADES = 'grades'

