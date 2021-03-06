from flask_restful import Resource, reqparse, inputs
from api.models.answer import AnswerModel
from api.models.question import QuestionModel
from flask_jwt import jwt_required, current_identity


class Answer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('answer', 
        type = inputs.regex('^[a-zA-Z0-9.,?@ ]{3,300}$'),
        required = True,
        help = "Please enter a valid answer."
    )

    """Get a specific answer to the question
    """
    def get(self, questionID, answerID):
        #Check if the question really exists
        #If True check for the answer and return
        #else, return a error message
        if QuestionModel.find_by_id(questionID):
            #Check for answer, returns an object
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                return AnswerModel.find_descriptive_single_answer(answerID), 200
            else:
                return {"message": "Answer not found."}, 422
        else:
            return {"message": "Cannot get answer for a non-existing question"},422

    """Update a specific answer to the question
    """
    @classmethod
    @jwt_required()
    def put(cls, questionID, answerID):
        data = cls.parser.parse_args()
        #check if the question exists
        #if exists, check for the answer
        #create a new answer object, update and return it
        #else return an error message
        if QuestionModel.find_by_id(questionID):
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                answer.answer = data['answer']
                if answer.update(questionID):
                    return {"message": "Your answer updated successfully"}, 201
            else:
                return {"message": "Cannot update a non-existing answer."}, 422
        else:
            return {"message": "Cannot update answer for a non-existing question."}, 422

    """Delete a specific answer to the question
    """
    @jwt_required()
    def delete(self, questionID, answerID):
        question = QuestionModel.find_by_id(questionID)
        if question:
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                answer.delete(questionID)
                return {"message": "Answer deleted successfully"}, 201
            else:
                return {"message": "Answer already deleted or does not exist."}, 422
        else:
            return {"message": "Cannot delete answer for a non-existing question."}, 422


class AnswerList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('answer', 
        type = inputs.regex('^[a-zA-Z0-9.,?@ ]{3,300}$'),
        required = True,
        help = "Please enter a valid answer."
    )

    @classmethod
    @jwt_required()
    def post(cls, questionID):
        #Check if the question exists
        #if True create an answer dictionary and pass it 
        #to add_answer method in answermodel(return the response)
        #else return error messages
        data = cls.parser.parse_args()

        identity = 0
        if current_identity.id:
            identity = current_identity.username

        if QuestionModel.find_by_id(questionID):
            if not AnswerModel.find_by_answer(questionID, data['answer']):
                answer = AnswerModel(data["answer"])
                if answer.add_answer(questionID, identity):
                    return {"message": "Answer inserted successfully"}, 201
            return {"message": "The answer already exists"}, 409

        return {"message": "You cannot answer a non-existing question"}, 422

    def get(self, questionID):
        #Check if the question exists
        #if True, return the answers
        #else, return an error message
        if QuestionModel.find_by_id(questionID):
            answers = AnswerModel.get_answers(questionID)
            if answers:
                return answers, 200
            return {"message": "There are no answers for this question"}, 422 #Unprocessable entity
        return {"message": "You can't find answers for a non existing question"}, 422 # Unp0rocessable entity


class AnswerUpVote(Resource):
        #Check if the question exists
        #if True create an answer object and upvote it
        #else return error messages
    @jwt_required()
    def put(self, questionID, answerID):
        question = QuestionModel.find_by_id(questionID)
        if question:
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                answer.upvote(questionID)
                return {"message": "Answer upvoted successfully"}, 201 #Created
            else:
                return {"message": "Cannot upvote for a non-existing answer."} , 422 #Unprocessable entity
        else:
            return {"message": "Cannot upvote answer for a non-existing question."}, 422 #Unprocessable entity

class AnswerDownVote(Resource):
    @jwt_required()
    def put(self, questionID, answerID):
        # parser = reqparse.RequestParser()
        # parser.add_argument('downvote', 
        #     type = str,
        #     required = True,
        #     help = "The upvote field is required"
        # )
        # data = parser.parse_args()
        question = QuestionModel.find_by_id(questionID)
        if question:
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                answer.downvote(questionID)
                return {"message": "Answer downvoted successfully"}, 201 #Created
            else:
                return {"message": "Cannot downvote for a non-existing answer."}, 422 #Unprocessable entity
        else:
            return {"message": "Cannot downvote answer for a non-existing question."}, 422 #Unprocessable entity
    
class SolveAnswer(Resource):
    @jwt_required()
    def put(self, questionID, answerID):

        question = QuestionModel.find_by_id(questionID)
        if question:
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                answer.solve(questionID)
                return {"message": "Answer marked as solution successfully"}, 201 #Created
            else:
                return {"message": "Cannot mark a non-existing answer as a solution."}, 422 #Unprocessable entity
        else:
            return {"message": "Cannot solve a non-existing question."}, 422 #Unprocessable entity