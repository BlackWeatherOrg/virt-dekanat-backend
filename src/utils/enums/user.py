from enum import Enum


class PermissionsEnum(Enum):
    VIEW_OWN_GRADES = 'view_own_grades'
    VIEW_COURSES = 'view_courses'
    VIEW_STUDENTS = 'view_students'
    EDIT_GRADES = 'edit_grades'
    MANAGE_ENROLLMENTS = 'manage_enrollments'
    VIEW_REPORTS = 'view_reports'
    MANAGE_USERS = 'manage_users'
    MANAGE_ROLES = 'manage_roles'
    MANAGE_PERMISSIONS = 'manage_permissions'


ROLE_PERMISSIONS = {
    'student': [
        PermissionsEnum.VIEW_OWN_GRADES,
        PermissionsEnum.VIEW_COURSES,
    ],
    'professor': [
        PermissionsEnum.VIEW_STUDENTS,
        PermissionsEnum.EDIT_GRADES,
        PermissionsEnum.VIEW_COURSES,
    ],
    'dean_office': [
        PermissionsEnum.MANAGE_ENROLLMENTS,
        PermissionsEnum.VIEW_REPORTS,
    ],
    'admin': [
        PermissionsEnum.MANAGE_USERS,
        PermissionsEnum.MANAGE_ROLES,
        PermissionsEnum.MANAGE_PERMISSIONS,
    ],
}
