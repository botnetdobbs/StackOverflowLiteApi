from flask_restful import Resource, reqparse
from api.models.answer import AnswerModel
from api.models.question import QuestionModel
from flask_jwt import jwt_required


class Answer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('answer', 
        type = str,
        required = True,
        help = "The answer field is required"
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
                return answer.json()
            else:
                return {"message": "Answer not found."}
        else:
            return {"message": "Cannot get answer for a non-existing question"}

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
                    return {"message": "Your answer updated successfully"}
            else:
                return {"message": "Answer not found."}
        else:
            return {"message": "Cannot update answer for a non-existing question."}

    """Delete a specific answer to the question
    """
    @jwt_required()
    def delete(self, questionID, answerID):
        question = QuestionModel.find_by_id(questionID)
        if question:
            answer = AnswerModel.find_by_id(questionID, answerID)
            if answer:
                answer.delete(questionID)
                return {"message": "Answer deleted successfully"} 
            else:
                return {"message": "Answer already deleted or does not exist.!"}
        else:
            return {"message": "Cannot delete answer for a non-existing question."}


class AnswerList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('answer', 
        type = str,
        required = True,
        help = "The answer field is required"
    )

    @classmethod
    @jwt_required()
    def post(cls, questionID):
        #Check if the question exists
        #if True create an answer dictionary and pass it 
        #to add_answer method in answermodel(return the response)
        #else return error messages
        data = cls.parser.parse_args()
        if QuestionModel.find_by_id(questionID):
            if not AnswerModel.find_by_answer(questionID, data['answer']):
                answer = AnswerModel(data["answer"])
                if answer.add_answer(questionID):
                    return {"message": "Answer inserted successfully"}
            return {"message": "The answer already exists"}

        return {"message": "You cannot answer a non-existing question"}, 403

    def get(self, questionID):
        #Check if the question exists
        #if True, return the answers
        #else, return an error message
        if QuestionModel.find_by_id(questionID):
            answers = AnswerModel.get_answers(questionID)
            if answers:
                return answers
            return {"message": "There are no answers for this question"}
        return {"message": "You can't find answers for a non existing question"}


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
                return {"message": "Answer upvoted successfully"} 
        else:
            return {"message": "Cannot upvote answer for a non-existing question."}

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
                return {"message": "Answer downvoted successfully"} 
        else:
            return {"message": "Cannot upvote answer for a non-existing question."}