from flask_restful import Resource, reqparse, inputs
from api.models.question import QuestionModel
from flask_jwt import current_identity, jwt_required

class Question(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', 
        type = inputs.regex('^[a-zA-Z0-9_-]{3,70}$'),
        required = True,
        help = 'Invalid question title.'
    )
    
    parser.add_argument('description',
        type = inputs.regex('^[a-zA-Z0-9_-]{3,300}$'),
        required = True,
        help = 'Invalid question description.'
    )

    def get(self, questionID):
        #Check if question exists
        #if true(returns an object) return it
        #else, return an error message
        question = QuestionModel.find_descriptive_single_question(questionID)
        if question:
            return question, 200
        return {"message": "Question not available."}, 422

    """Process the PUT request for updating specific a question
    """
    @classmethod
    @jwt_required()
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
                    return QuestionModel.find_descriptive_single_question(questionID), 200
                return {"message": "Question could not be updated."}, 409
            return {"message": "You can't edit a non-existing question."}, 422
        return {"message": "Question with the same decription already exists."}, 422

    @jwt_required()
    def delete(self, questionID):
        #Check if the question really exists
        #if True call the delete method and return a success message
        #else, return an error message
        question = QuestionModel.find_by_id(questionID)
        if question:
            if question.delete():
                return {"message": "Question deleted successfully."}, 201
            else:
                return {"message": "Question not deleted."}, 409 #Confilict
        return {"message": "The question is not available or it was already deleted."}, 422 #Unprocessable entity

class QuestionList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', 
        type = inputs.regex('^[a-zA-Z0-9]{3,70}$'),
        required = True,
        help = 'Invalid question title.'
    )
    
    parser.add_argument('description',
        type = inputs.regex('^[a-zA-Z0-9]{3,300}$'),
        required = True,
        help = 'Invalid question description.'
    )

    """Process the POST request for adding a question
    """
    @jwt_required()
    def post(self):
        data = QuestionList.parser.parse_args()
        #Get the identity of the currently logged in user
        identity = 0
        if current_identity.id:
            identity = current_identity.id
        else:
            return {"message": "Login to continue"}
        #Check if a question with the same description exists
        #return an error message if it exists
        #else, save the new question and return a response
        if QuestionModel.find_by_description(data['description']):
            return {"message": "The question is already asked"}, 409 # Conflict(Duplicate)

        #Create a question object and pass the arguments
        question = QuestionModel(data["title"], data["description"])

        response = question.save(identity)
        return response, 201

    """Process the POST request for adding a question
    """
    def get(self):
        #call the all classmethod of questionModel class to get the response
        #if response exists , return it
        #else, return an error message
        response = QuestionModel.all()
        if response:
            return response, 200

        return {"message": "No questions found!"}, 422 #Unprocessable entity

        