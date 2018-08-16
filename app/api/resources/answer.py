from flask_restful import Resource, reqparse
from api.models.answer import AnswerModel
from api.models.question import QuestionModel


class Answer(Resource):

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


class AnswerList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('answer', 
        type = str,
        required = True,
        help = "The answer field is required"
    )

    @classmethod
    def post(cls, questionID):
        #Check if the question exists
        #if True create an answer dictionary and pass it 
        #to add_answer method in answermodel(return the response)
        #else return error messages
        data = cls.parser.parse_args()
        if QuestionModel.find_by_id(questionID):
            answer = {"answer": data["answer"]}
            return AnswerModel.add_answer(questionID, answer), 201

        return {"message": "You cannot answer a non-existing question"}, 403
