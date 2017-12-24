import unittest
from flask import Flask


class FirstTest(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_connect(self):
        r = self.app.get('http://127.0.0.1:8000/')
        self.assertEqual(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()
