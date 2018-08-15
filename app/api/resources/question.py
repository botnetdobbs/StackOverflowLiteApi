from flask_restful import Resource, reqparse
from api.models.question import QuestionModel

class Question(Resource):
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

    def get(self, questionID):
        #Check if question exists
        #if true(returns an object) return it
        #else, return an error message
        question = QuestionModel.find_by_id(questionID)
        if question:
            return question.json(), 200
        return {"message": "Question not available."}, 404

    """Process the PUT request for updating specific a question
    """
    @classmethod
    def put(cls, questionID):
        #Check if the question description already exists
        #if it exists return an error message
        #if not, check if the question identified by id exists
        #if true, update the question and return
        #else, return an error message
        data = cls.parser.parse_args()
        if not QuestionModel.find_by_description(data['description']):
            question = QuestionModel.find_by_id(questionID)
            if question:
                #create a new object with updated details
                updated_question = QuestionModel(data['title'], data['description'], question.id)
                #Update and return json data
                if updated_question.update():
                    return updated_question.json()
                return {"message": "Item could not be updated"}
            return {"message": "Item does not exist."}
        return {"message": "Question with the same decription already exists."}

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
        #Check if a question with the same description exists
        #return an error message if it exists
        #else, save the new question and return a response
        if QuestionModel.find_by_description(data['description']):
            return {"message": "The question is already asked"}

        #Create a question object and pass the arguments
        question = QuestionModel(data["title"], data["description"])

        response = question.save()

        return response, 201

    """Process the POST request for adding a question
    """
    def get(self):
        #call the all classmethod of questionModel class to get the response
        #if response exists , return it
        #else, return an error message
        response = QuestionModel.all()
        if response:
            return response

        return {"message": "No questions found!"}
        