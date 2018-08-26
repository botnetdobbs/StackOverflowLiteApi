# test_bucketlist.py
import unittest
from api import app
from tests.main import reset_question

class StackOverflowApiTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.question = {'title': 'This is a sample question title', 'description': 'This is a sample question description'}


    def test_question_creation(self):
        """Test API can create a new question (POST request)"""
        res = self.client().post('/api/v1/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        self.assertIn('This is a sample', str(res.data))

    def test_get_all_questions(self):
        """Test API can get all the questions (GET request)."""
        res = self.client().post('/api/v1/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    def test_api_can_get_single_question(self):
        """Test API can get a single question by using it's unique id."""
        res = self.client().post('/api/v1/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/v1/questions/1')
        self.assertEqual(res.status_code, 200)

    def test_bucketlist_can_be_edited(self):
        """Test API can edit a specific question. (PUT request)"""
        res = self.client().post('/api/v1/questions', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().put(
            '/api/v1/questions/1',
            data={
                "title": "new title",
                "description": "New updated description"
            })
        self.assertEqual(res.status_code, 200)

    # def test_bucketlist_deletion(self):
    #     """Test API can delete an existing bucketlist. (DELETE request)."""
    #     res = self.client().post('/api/v1/questions', data=self.question)
    #     self.assertEqual(res.status_code, 201)
    #     res = self.client().delete('/api/v1/questions/1', data=self.question)
    #     self.assertEqual(res.status_code, 200)
    #     # Test to see if it exists, should return a 404
    #     result = self.client().get('/api/v1/questions/1')
    #     self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # clear the question list
            reset_question()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()