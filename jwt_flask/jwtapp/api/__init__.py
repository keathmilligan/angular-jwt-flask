"""
RESTful API views
"""

import os.path
from .. import app  # noqa


@app.after_request
def after_request(response):
    """
    Post request processing - add CORS, cache control headers
    """
    # Enable CORS requests for local development
    # The following will allow the local angular-cli development environment to
    # make requests to this server (otherwise, you will get 403s due to same-
    # origin poly)
    response.headers.add('Access-Control-Allow-Origin',
                         'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,Set-Cookie,Cookie,Cache-Control,Pragma,Expires')  # noqa
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE')

    # disable caching all requests
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    return response


# load all views in this directory
__all__ = [os.path.basename(p)[:-3]
           for p in os.listdir(os.path.dirname(__file__))
           if p.endswith('.py') and not p.startswith('_')]
