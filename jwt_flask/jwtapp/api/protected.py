"""
Protected APIs
"""

from flask import request, make_response, abort
from flask.json import jsonify
from .. import app
from ..auth import auth_required, admin_required


@app.route('/api/user-sample', methods=['GET', 'POST'])
@auth_required
def sample_api():
    """
    Example API
    """
    if request.method == 'GET':
        return make_response(jsonify({'example': 123}))
    elif request.method == 'POST':
        data = request.get_json()
        app.logger.debug('payload: %d', data['example'])
        return make_response(jsonify({'example': data['example'] * 2}))
    else:
        abort(405)


@app.route('/api/admin-sample', methods=['GET', 'POST'])
@admin_required
def admin_api():
    """
    Example API
    """
    if request.method == 'GET':
        return make_response(jsonify({'example': 123}))
    elif request.method == 'POST':
        data = request.get_json()
        app.logger.debug('payload: %d', data['example'])
        return make_response(jsonify({'example': data['example'] * 2}))
    else:
        abort(405)
