#Import the connection
from api.db import connect
from api import bcrypt

class UserModel:
    """Initialize the class, the _id being
                an optional parameter
        used _id since id is a Python keyword
    """
    def __init__(self, username, password, _id=None):
        self.id = _id
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

    def save(self):
        #Save the object to the database
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO users (username, password) VALUES(%s, %s)", (self.username, self.password))
    """Find a user uniquely identified by the username
    """
    @classmethod
    def get_by_username(cls, username):
        #Save the connection as connection
        #Get the cursor fro0m the connection variable
        #No need to commit, Once the program exits the with block
        #It will automatically commit and close the connection
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                user = cursor.fetchone()
                if user:
                    return cls(user[1], user[2], user[0])
                else:
                    return None

    """Find a user uniquely identified by the ID
    """
    @classmethod
    def get_by_id(cls, user_id):
        #Save the connection as connection
        #Get the cursor from the connection variable
        #No need to commit, Once the program exits the with block
        #It will automatically commit and close the connection
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE id = %d", (user_id,))
                user = cursor.fetchone()
                return cls(user[1], user[2], user[0])

#With this approach we have to create a connection each time we need it hence
# possible overhead performance costs.
#Connection pooling can help solve the issue.
#http://initd.org/psycopg/docs/pool.html
        