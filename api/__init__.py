from flask import Flask, render_template, jsonify
from flask_restful import Api
#Import the Bcrypr class for password hashing
from flask_bcrypt import Bcrypt
from datetime import timedelta
from api.resources.question import Question, QuestionList
from api.resources.answer import Answer, AnswerList
from api.resources.user import UserRegister

from api.verify import authenticate, identity

from flask_jwt import JWT


app = Flask(__name__)
#pass the flask app object to the Bcrypt class and store in bcrypt
bcrypt = Bcrypt(app)
app.secret_key = 'xbt3ybot9'
api = Api(app)
#Custom authentification endpoint
app.config['JWT_AUTH_URL_RULE'] = '/api/v1/auth/login'
#Custom jwt timeout token to expire after an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)

jwt = JWT(app, authenticate, identity) # Createa a new endpoint (/auth) default. Overriden above
#Register the resources
api.add_resource(QuestionList, '/api/v1/questions')
api.add_resource(Question, '/api/v1/questions/<int:questionID>')

api.add_resource(AnswerList, '/api/v1/questions/<int:questionID>/answers')
api.add_resource(Answer, '/api/v1/questions/<int:questionID>/answers/<int:answerID>')

api.add_resource(UserRegister, '/api/v1/auth/register')

@app.route('/')
def home():
    return render_template('index.html')

