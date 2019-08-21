"""
Authentication Functions
"""

from functools import wraps
from flask import abort
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt_identity,
    verify_jwt_in_request, verify_jwt_refresh_token_in_request
)
from . import app


USERS = [
    {
        'username': 'admin',
        'password': 'admin',
        'enabled': True,
        'is_admin': True
    },
    {
        'username': 'user',
        'password': 'user',
        'enabled': True,
        'is_admin': False
    }
]


class AuthenticationError(Exception):
    """Base Authentication Exception"""
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return self.__class__.__name__ + '(' + str(self.msg) + ')'


class InvalidCredentials(AuthenticationError):
    """Invalid username/password"""


class AccountInactive(AuthenticationError):
    """Account is disabled"""


class AccessDenied(AuthenticationError):
    """Access is denied"""


class UserNotFound(AuthenticationError):
    """User identity not found"""


def authenticate_user(username, password):
    """
    Authenticate a user
    """
    for user in USERS:
        if username == user['username'] and password == user['password']:
            if user['enabled']:
                return (
                    create_access_token(identity=username),
                    create_refresh_token(identity=username)
                )
            else:
                raise AccountInactive(username)
    else:
        raise InvalidCredentials()


def get_authenticated_user():
    """
    Get authentication token user identity and verify account is active
    """
    identity = get_jwt_identity()
    for user in USERS:
        if identity == user['username']:
            if user['enabled']:
                return user
            else:
                raise AccountInactive()
    else:
        raise UserNotFound(identity)


def deauthenticate_user():
    """
    Log user out
    in a real app, set a flag in user database requiring login, or
    implement token revocation scheme
    """
    identity = get_jwt_identity()
    app.logger.debug('logging user "%s" out', identity)


def refresh_authentication():
    """
    Refresh authentication, issue new access token
    """
    user = get_authenticated_user()
    return create_access_token(identity=user['username'])


def auth_required(func):
    """
    View decorator - require valid access token
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        try:
            get_authenticated_user()
            return func(*args, **kwargs)
        except (UserNotFound, AccountInactive) as error:
            app.logger.error('authorization failed: %s', error)
            abort(403)
    return wrapper


def auth_refresh_required(func):
    """
    View decorator - require valid refresh token
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_refresh_token_in_request()
        try:
            get_authenticated_user()
            return func(*args, **kwargs)
        except (UserNotFound, AccountInactive) as error:
            app.logger.error('authorization failed: %s', error)
            abort(403)
    return wrapper


def admin_required(func):
    """
    View decorator - required valid access token and admin access
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        try:
            user = get_authenticated_user()
            if user['is_admin']:
                return func(*args, **kwargs)
            else:
                abort(403)
        except (UserNotFound, AccountInactive) as error:
            app.logger.error('authorization failed: %s', error)
            abort(403)
    return wrapper
