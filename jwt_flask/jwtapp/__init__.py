"""
Flask JWT Example
"""

import sys
import os.path
from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_json(os.path.join('resources', 'config.json'))

jwt = JWTManager(app)


# override debug flag
if '--debugger' in sys.argv:
    app.debug = True

# register error handlers
from . import errors  # noqa: F401

# load & register APIs
from .api import *  # noqa: F401,F403
