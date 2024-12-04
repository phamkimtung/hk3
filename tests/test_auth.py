import unittest
from app import app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_register(self):
        response = self.client.post('/auth/register', json={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
