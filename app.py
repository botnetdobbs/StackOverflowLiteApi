from flask import Flask
from flask_restful import Api

from api.resources.question import Question, QuestionList
from api.resources.answer import Answer, AnswerList


app = Flask(__name__)

api = Api(app)

#Register the resources
api.add_resource(QuestionList, '/api/v1/questions')
api.add_resource(Question, '/api/v1/questions/<int:questionID>')

api.add_resource(AnswerList, '/api/v1/questions/<int:questionID>/answers')
api.add_resource(Answer, '/api/v1/questions/<int:questionID>/answers/<int:answerID>')


"""To prevent the app from running when the file or something in the file is imported
i.e if the file is run, the flask app will start, 
but if another file that imports app runs then it will not start
"""
if __name__ == '__main__':
    app.run(port=5000, debug=True)