from flask_restful import Resource, reqparse
from api.models.answer import AnswerModel
from api.models.question import QuestionModel


class Answer(Resource):
    pass


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

    def get(self, questionID):
        #Check if the question exists
        #If true get the answers for the question
        #else return error messages 
        if QuestionModel.find_by_id(questionID):
            return AnswerModel.get_answers(questionID)

        return {"message": "You can't find answers for a non existing question"}