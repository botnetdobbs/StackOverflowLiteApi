users = []

class UserModel:
    """Initialize the class, the _id being
                an optional parameter
        used _id since id is a Python keyword
    """
    def __init__(self, username, password, _id=None):
        self.id = _id
        self.username = username
        self.password = password

    def save(self):
        #Save the object to the list as dictionary
        user_id = 1
        #Check if a questions are available
        if len(users) > 0:
            #Add id(auto increment to the question id)
            user_id = users[-1]["id"] + 1
        #Create a new question dictionary
        new_user = {
            "id": user_id,
            "username": self.username,
            "password": self.password,
        }
        #append the dictionsry to the questions list
        users.append(new_user)
        return True

    """Find a user uniquely identified by the username
    """
    @classmethod
    def get_by_username(cls, username):
        for user in users:
            if user['username'] == username:
                return cls(user['username'], user['password'], user['id'])

    """Find a user uniquely identified by the ID
    """
    @classmethod
    def get_by_id(cls, user_id):
        for user in users:
            if user.id == id:
                return cls(user['username'], user['password'], user['id'])
        