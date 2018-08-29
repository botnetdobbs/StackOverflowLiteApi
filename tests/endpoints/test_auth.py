import unittest
import json
from api import app
from api.db import connect
from tests.modules_for_t import teardown
from api.create_tables import create_tables
from flask import Response

class AuthTestCase(unittest.TestCase):
    """Test the authentification endpoints
    """

    def setUp(self):
        """Set up test variables."""
        # initialize the test client
        self.app = app


        self.client = self.app.test_client

        # This is the user test json data with a predefined email and password
        self.new_user = {
            'username': 'example_user',
            "email": "test@test.com",
            'password': 'example_password'
        }

        with self.app.app_context():
            teardown()


    def test_registration(self):
        """Test user registration.
        """
        res = self.client().post('/api/v2/auth/register', data=self.new_user)
        # get the results returned in json format
        result = json.loads(res.data.decode())
        # assert that the request contains a success message and a 201 status code
        self.assertEqual(result['message'], "User created successfully")
        self.assertEqual(res.status_code, 201)

    def test_already_registered_user(self):
        """Test for duplicate registration
        """
        res = self.client().post('/api/v2/auth/register', data=self.new_user)
        self.assertEqual(res.status_code, 201)
        second_res = self.client().post('/api/v2/auth/register', data=self.new_user)
        self.assertEqual(second_res.status_code, 409)
        # get the results returned in json format
        result = json.loads(second_res.data.decode())
        self.assertEqual(
            result['message'], "The username already exists")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main() 