import sqlite3
import unittest
from storage import get_data


class TestPhoneNumbersDb(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
        self.address = 'Исанова 4'
        self.cursor.execute("INSERT INTO address VALUES (NULL, ?)",
                            (self.address,))
        self.conn.commit()

    @classmethod
    def tearDownClass(self):
        pass

    def test_get_phone_number(self):
        self.cursor.execute("SELECT * FROM address WHERE"
                            " id=(SELECT max(id) FROM address);")
        last_address = self.cursor.fetchone()
        self.assertEqual(get_data.get_address('mydatabase.db'), last_address)
