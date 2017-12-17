import sqlite3
import unittest


class TestPhoneNumbersDb(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
        self.variable = +996700080977
        self.cursor.execute("INSERT INTO phone_number VALUES (NULL, ?)",
                            (self.variable,))
        self.conn.commit()

    @classmethod
    def tearDown(self):
        pass
