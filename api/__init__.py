from flask import Flask, render_template
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

@app.route('/')
def home():
    return render_template('index.html')

