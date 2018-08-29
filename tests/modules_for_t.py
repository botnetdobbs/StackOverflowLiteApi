from api.db import connect
from api.models.user import UserModel

def teardown():
    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA IF EXISTS public CASCADE")

def create_user():
    new_user = UserModel('lazarus', 'test@test.com', 'xbt3ybot9')
    new_user.save()