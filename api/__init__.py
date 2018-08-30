from flask import Flask, render_template, jsonify
from flask_restful import Api
from datetime import timedelta
from api.resources.question import Question, QuestionList
from api.resources.answer import Answer, AnswerList, AnswerUpVote, AnswerDownVote, SolveAnswer
from api.resources.user import UserRegister, UserList

from api.verify import authenticate, identity
from api.create_tables import create_tables

from flask_jwt import JWT


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object('config.ProductionConfig')
create_tables()
api = Api(app) 

#Custom authentification endpoint
app.config['JWT_AUTH_URL_RULE'] = '/api/v2/auth/login'

#Get message when user ain't logged in 
app.config['PROPAGATE_EXCEPTIONS'] = True
#Custom jwt timeout token to expire after an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)

jwt = JWT(app, authenticate, identity) # Createa a new endpoint (/auth) default. Overriden above
#Register the resources
api.add_resource(QuestionList, '/api/v2/questions')
api.add_resource(Question, '/api/v2/questions/<int:questionID>')

api.add_resource(AnswerList, '/api/v2/questions/<int:questionID>/answers')
api.add_resource(Answer, '/api/v2/questions/<int:questionID>/answers/<int:answerID>')
#Endpoint for upvote
api.add_resource(AnswerUpVote, '/api/v2/questions/<int:questionID>/answers/<int:answerID>/upvote')
#Endpoint for downvote
api.add_resource(AnswerDownVote, '/api/v2/questions/<int:questionID>/answers/<int:answerID>/downvote')
api.add_resource(SolveAnswer, '/api/v2/questions/<int:questionID>/answers/<int:answerID>/solved')

api.add_resource(UserRegister, '/api/v2/auth/register')

api.add_resource(UserList, '/api/v2/user/questions')

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "The resource cannot be found"}), 404

