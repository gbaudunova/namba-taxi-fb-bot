import os
import sqlite3
import unittest
from .get_data import get_data


class TestPhoneNumbersDb(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        variable = +996700080977
        cursor.execute("INSERT INTO phone_number VALUES (NULL, ?)", (variable,))
        cursor.execute("SELECT * FROM phone_number WHERE "
                       "id=(SELECT max(id) FROM phone_number);")
        phone_number = cursor.fetchone()
        conn.commit()

    def tearDown(self):
        """
        Delete the database
        """
        os.remove("mydatabase.db")

    def test_get_phone_number(self):
        num = +996700080977
        values = [(+996700080977, +996702124403)]
        self.assertEqual(get_data(), values)

