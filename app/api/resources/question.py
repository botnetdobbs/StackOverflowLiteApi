from flask_restful import Resource, reqparse
from models.question import QuestionModel

class Question(Resource):
    pass


class QuestionList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', 
        type = str,
        required = True,
        help = 'The title field is required.'
    )
    
    parser.add_argument('description',
        type = str,
        required = True,
        help = 'The description field is required.'
    )

    """Process the POST request for adding a question
    """
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        #Create a question object and pass the arguments
        question = QuestionModel(data["title"], data["description"])

        response = question.save()

        return response, 201