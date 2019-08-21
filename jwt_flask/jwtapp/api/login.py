"""
Login/logout APIs
"""

from flask import request, make_response, abort
from flask.json import jsonify
from .. import app
from ..auth import (authenticate_user, deauthenticate_user,
                    refresh_authentication, get_authenticated_user,
                    auth_required, auth_refresh_required, AuthenticationError)


@app.route('/api/auth/login', methods=['POST'])
def login_api():
    """
    Login user
    """
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        access_token, refresh_token = authenticate_user(username, password)
        return make_response(jsonify({
            'accessToken': access_token,
            'refreshToken': refresh_token
        }))
    except AuthenticationError as error:
        app.logger.error('authentication error: %s', error)
        abort(403)


@app.route('/api/auth/info', methods=['GET'])
@auth_required
def login_info_api():
    """
    Get informaiton about currently logged in user
    """
    try:
        user = get_authenticated_user()
        return make_response(jsonify({
            'username': user['username'],
            'enabled': user['enabled'],
            'isAdmin': user['is_admin']
        }))
    except AuthenticationError as error:
        app.logger.error('authentication error: %s', error)
        abort(403)


@app.route('/api/auth/logout', methods=['POST'])
@auth_refresh_required
def logout_api():
    """
    Log user out
    """
    deauthenticate_user()
    return make_response()


@app.route('/api/auth/refresh', methods=['POST'])
@auth_refresh_required
def refresh_api():
    """
    Get a fresh access token from a valid refresh token
    """
    try:
        access_token = refresh_authentication()
        return make_response(jsonify({
            'accessToken': access_token
        }))
    except AuthenticationError as error:
        app.logger.error('authentication error %s', error)
        abort(403)
