from api.models.user import UserModel as User
from api import bcrypt

#Referenced on Flask_JWT on https://pythonhosted.org/Flask-JWT/
def authenticate(username, password):
    user = User.get_by_username(username)
    if bcrypt.check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    user = User.get_by_id(user_id)
    return user