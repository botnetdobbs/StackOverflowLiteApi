from functools import wraps
from flask import current_app
from flask_jwt import _jwt_required, current_identity

"""Custom decorator to get the current_identity
"""
def jwt_optionnal(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                _jwt_required(realm or current_app.config['JWT_DEFAULT_REALM'])
            except:
                pass
            return fn(*args, **kwargs)
        return decorator
    return wrapper
