from flask_restful import Resource, reqparse, inputs
from api.models.user import UserModel
from api.models.question import QuestionModel

from flask_jwt import current_identity, jwt_required
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = inputs.regex('^[a-z0-9_-]{3,15}$'),
        required = True,
        help = "Please enter a valid username"
    )
    parser.add_argument('email',
        type = inputs.regex('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
        required = True,
        help = 'Invalid email address'
    )
    parser.add_argument('password',
        type = inputs.regex('[A-Za-z0-9@#$%^&+=]{8,}'),
        required = True,
        help = "The password is not strong enough"
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
        if UserModel.get_by_email(data['email']):
            return {"message": "The email already exists"}, 409

        user = UserModel(data['username'], data['email'], data['password'])
        user.save()
        return {"message": "User created successfully"}, 201


class UserList(Resource):
    """Get all questions belonging to the user
    """
    @jwt_required()
    def get(self):
        #Get the identity of the currently logged in user
        identity = 0
        if current_identity.id:
            identity = current_identity.id
        else:
            return {"message": "login to continue"}

        #Check if the user has questions
        my_questions = QuestionModel.find_by_user_id(identity)
        if my_questions:
            return my_questions
        else:
            return {"message": "You currently have no questions."}