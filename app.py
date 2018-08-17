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

@app.route('/')
def home():
    return """Testing only available through Postman.\n\n
    Add the following at the end of the Url:- 'api/v1/questions'...,\n
    1. Posting a question\n
    - POST _https://zstackoverflowliteapi.herokuapp.com/api/v1/question_\n\n

    2. Fetch all questions\n
    - GET _https://zstackoverflowliteapi.herokuapp.com/api/v1/question_\n\n

    3. Fetch a specific question\n
    - GET _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>_\n\n

    4. Edit a specific question\n
    - PUT _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>_\n\n

    5. Delete a specific question\n
    - DELETE _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>_\n\n

    6. Posting an answer to the specific question\n
    - POST _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>/answers_\n\n

    7. Fetch an answer(s) to the specific question\n
    - GET _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>/answers_\n\n

    8. Fetch a specific answer from a specific question\n
    - GET _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>/answers<<int:answerID>>_\n\n

    9. Edit a specific answer from a specific question\n
    - PUT _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>/answers<<int:answerID>>_\n\n

    10. Delete a specific answer from a specific question\n
    - DELETE _https://zstackoverflowliteapi.herokuapp.com/api/v1/question/<int:questionID>/answers<<int:answerID>>_\n

    NB:-Unique Identifiers\n
    > <int:questionID>\n
    > <int:answerID>\n\n
    
    NB:- You can save yourself the burden of typing the long url using Postman variables\n
    http://blog.getpostman.com/2014/02/20/using-variables-inside-postman-and-collection-runner/"""


"""To prevent the app from running when the file or something in the file is imported
i.e if the file is run, the flask app will start, 
but if another file that imports app runs then it will not start
"""
if __name__ == '__main__':
    app.run(port=5000, debug=True)