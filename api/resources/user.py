from flask_restful import Resource, reqparse, inputs
from api.models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = inputs.regex('[a-zA-Z0-9]'),
        required = True,
        help = "Please enter a valid username"
    )
    parser.add_argument('email',
        type = inputs.regex('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
        required = True,
        help = 'Invalid email address'
    )
    parser.add_argument('password',
        type = str,
        required = True,
        help = "The password field is required"
    )
    """
    Handle the post request to register user
    """
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        #Check if the username already exists
        #if True, return an error message
        #else, create a new user object, save it and return a success message
        if UserModel.get_by_username(data['username']):
            return {"message": "The username already exists"}, 409

        user = UserModel(data['username'], data['email'], data['password'])
        user.save()
        return {"message": "User created successfully"}, 201