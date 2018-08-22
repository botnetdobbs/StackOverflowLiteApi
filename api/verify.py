from api.models.user import UserModel as User

#Referenced on Flask_JWT on https://pythonhosted.org/Flask-JWT/
def authenticate(username, password):
    user = User.get_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    user = User.get_by_id(user_id)
    return user