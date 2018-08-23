# test_bucketlist.py
import unittest
import os
import json
from app import app

class EndpointsTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client
        self.question = {'title': 'This is my sample title',
                            'description': 'This is the description of qoing to Borabora'
                    }

    def test_question_creation(self):
        """Test if the API can create a question (POST request)"""
        res = self.client().post('/api/v1/questions')
        self.assertEqual(res.status_code, 201)

    def test_get_all_questions(self):
        """Test if the API can get questions (GET request)."""
        res = self.client().get(
            '/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    def test_get_questions_by_id(self):
        """Test if the API can get a single question by using it's id."""
        rv = self.client().post('/api/v1/questions/1')
        self.assertEqual(rv.status_code, 200)

    def test_bucketlist_can_be_edited(self):
        """Test API can edit an existing bucketlist. (PUT request)"""
        rv = self.client().put(
            '/api/v1/questions/1',
            data={
                "title": "Edit1",
                "description": "The description update1"
            })
        self.assertEqual(rv.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()