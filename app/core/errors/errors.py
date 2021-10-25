"""Module custom error code"""

from . import AppBaseException


class UsernameExist(AppBaseException):
    status_code = 400
    msg = "Username Exists"


class UnknownError(AppBaseException):
    status_code = 500
    msg = "Internal Server Error"
