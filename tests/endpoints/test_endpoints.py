import unittest
from api import app
import json
from tests.modules_for_t import teardown
from api.create_tables import create_tables
from api.db import connect


class EndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app

        self.client = app.test_client
        self.question = {
            "title": "This is title 1",
            "description": "This is description 1"
        }
        self.question1 = {
            "title": "This is title 1",
            "description": "This is description 2"
        }
        self.answer = {
            "answer": "This is answer 1"
        }
        self.answer1 = {
            "answer": "This is answer 2"
        }

        with self.app.app_context():
            teardown()

    def register_user(self):
        user = {
            "username": "username1",
            "email" : "test@test.com",
            "password": "password1"
        }
        return self.client().post('/api/v2/auth/register',
        headers = {
            "Content-Type" : 'application/json'}, 
        data = json.dumps(user))

    def login_user(self):
        user = {
            "username": "username1",
            "password": "password1"
        }
        return self.client().post('/api/v2/auth/login', 
        headers = 
            {"Content-Type" : 'application/json'}, 
        data=json.dumps(user))
    def test_for_create_question(self):
        #Register the user
        self.register_user()
        #Login the user and get the response
        response = self.login_user()
        #Get the access token
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        # print(access_token)
        #Post the question
        create_question = self.client().post('/api/v2/questions', 
        headers = {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        #Check the status code
        self.assertEqual(create_question.status_code, 201)
        #Check if the string exists in the resulting response
        self.assertIn('Question created successfully.', str(create_question.data))
        
    
    def test_for_get_all_questions(self):
        #Register the user
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        #Get the token
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        #Add a question
        add_question = self.client().post('/api/v2/questions', 
        headers = {
            "Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
        data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
        #Get the questions, check the status code and if the string is in the response
        get_questions = self.client().get('/api/v2/questions')
        self.assertEqual(get_questions.status_code, 200)
        self.assertIn('This is title 1', str(get_questions.data))

    def test_for_find_question_by_id(self):
        #Register a user and login(returns a response)
        self.register_user()
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = {
            "Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
        #Get the question, check the status code and if the string is in the response
        get_question = self.client().get('/api/v2/questions/1', 
        headers = {
            "Authorization" : 'JWT ' + access_token})
        self.assertEqual(get_question.status_code, 200)
        self.assertIn('This is description 1', str(get_question.data))

    def test_for_edit_question(self):
        #Register a user and login(returns a response)
        self.register_user()
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
#Edit the question, check the status code and if the string is in the response
        edit_question = self.client().put('api/v2/questions/1', 
        headers = {"Content-Type": "application/json",
                "Authorization": "JWT " + access_token},
                data = json.dumps(self.question1))
        self.assertEqual(edit_question.status_code, 200)
        self.assertIn('This is title 1', str(edit_question.data))

    def test_for_delete_question(self):
        #Register a user and login(returns a response)
        self.register_user()
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
        #Delete the question, check the status code and if the string is in the response
        delete_question = self.client().delete('/api/v2/questions/1', 
        headers = {"Authorization" : 'JWT ' + access_token})
        self.assertEqual(delete_question.status_code, 201)
        self.assertIn("Question deleted successfully.", str(delete_question.data))
    
    def test_for_create_answer(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
        #Add the answers, check the status code and if the string is in the response
        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        self.assertIn('Answer inserted successfully', str(add_answer.data))
    
    def test_for_get_all_answers(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
        #Add the answer
        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
            #Check the status code
        self.assertEqual(add_answer.status_code, 201)
        #Get the answers and check the status code & the string in the response
        get_answers = self.client().get('/api/v2/questions/1/answers')
        self.assertEqual(get_answers.status_code, 200)
        self.assertIn('This is answer 1', str(get_answers.data))
    
    def test_for_get_single_answer(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)
        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        #Get the answer and check the status code & the string in the response
        get_answer = self.client().get('/api/v2/questions/1/answers/1')
        self.assertEqual(get_answer.status_code, 200)
        self.assertIn('This is answer 1', str(get_answer.data))
    
    def test_for_edit_answer(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)

        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        #Edit the answers and check the status code & the string in the response
        edit_answer = self.client().put('/api/v2/questions/1/answers/1', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer1))
        self.assertEqual(edit_answer.status_code, 201)
        self.assertIn('updated', str(edit_answer.data))
    
    def test_for_upvote_answer(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)

        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        #Upvote the answer and check the status code & the string in the response
        upvote_answer = self.client().put('/api/v2/questions/1/answers/1/upvote', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token})
        self.assertEqual(upvote_answer.status_code, 201)
        self.assertIn('upvoted', str(upvote_answer.data))
    
    def test_for_downvote_answer(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)

        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        #Downvote the answer and check the status code & the string in the response
        downvote_answer = self.client().put('/api/v2/questions/1/answers/1/downvote', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token})
        self.assertEqual(downvote_answer.status_code, 201)
        self.assertIn('downvoted successfully', str(downvote_answer.data))

    def test_for_delete_answer(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)

        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        #Delete the answer and check the status code & the string in the response
        delete_answer = self.client().delete('/api/v2/questions/1/answers/1', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token})
        self.assertEqual(delete_answer.status_code, 201)
        self.assertIn('successfully', str(delete_answer.data))

    def test_for_mark_answer_as_solved(self):
        #Register a user and login(returns a response)
        self.register_user()
        #Login aand get the response
        response = self.login_user()
        res = json.loads(response.data.decode())
        access_token = res["access_token"]
        print(access_token)
        add_question = self.client().post('/api/v2/questions', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.question))
        self.assertEqual(add_question.status_code, 201)

        add_answer = self.client().post('/api/v2/questions/1/answers', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token},
            data = json.dumps(self.answer))
        self.assertEqual(add_answer.status_code, 201)
        #Mark the answer and check the status code & the string in the response
        mark_answer = self.client().put('/api/v2/questions/1/answers/1/solved', 
        headers = 
            {"Content-Type" : 'application/json',
            "Authorization" : 'JWT ' + access_token})
        self.assertEqual(mark_answer.status_code, 201)
        self.assertIn('solution', str(mark_answer.data))


if __name__ == "__main__":
    unittest.main()