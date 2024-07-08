from flask_jwt_extended import get_jwt , verify_jwt_in_request
from functools import wraps
from .get_role import get_role

# creating the role custom function to check if one is admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args , **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if not get_role(claims['roles'], 'administrator'):
            return dict(status='fail', message='unauthorised'), 403
        return fn(*args, **kwargs)
    return wrapper