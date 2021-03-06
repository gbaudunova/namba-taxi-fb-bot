import sqlite3
import unittest
from storage import get_data
from config import db_config


class TestPhoneNumbersDb(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.conn = sqlite3.connect(db_config.db_conf['name'])
        self.cursor = self.conn.cursor()
        self.address = 'Исанова 5'
        self.number = +996700080577
        self.fare = 2
        self.order_id = 65985274
        self.cursor.execute("INSERT INTO address VALUES\
                            (NULL, ?)", (self.address,))
        self.cursor.execute("INSERT INTO phone_number VALUES\
                            (NULL, ?)", (self.number,))
        self.cursor.execute("INSERT INTO fare VALUES \
                            (NULL, ?)", (self.fare,))
        self.cursor.execute('INSERT INTO order_id VALUES\
                            (NULL , ?)', (self.order_id,))
        self.conn.commit()

    @classmethod
    def tearDownClass(self):
        self.conn = sqlite3.connect(db_config.db_conf['name'])
        self.cursor = self.conn.cursor()
        self.cursor.execute('DELETE FROM order_id WHERE \
                            id=(SELECT max(id) FROM order_id);')
        self.cursor.execute('DELETE FROM address WHERE \
                            id=(SELECT max(id) FROM address);')
        self.cursor.execute('DELETE FROM phone_number WHERE \
                            id=(SELECT max(id) FROM phone_number);')
        self.cursor.execute('DELETE FROM fare WHERE \
                            id=(SELECT max(id) FROM fare);')
        self.conn.commit()

    def test_get_address(self):
        self.cursor.execute("SELECT * FROM address WHERE \
                            id=(SELECT max(id) FROM address);")
        last_address = self.cursor.fetchone()
        self.assertEqual(get_data.get_address(db_config.db_conf['name']),
                         last_address)

    def test_get_order_id(self):
        self.cursor.execute("SELECT * FROM order_id WHERE \
                            id=(SELECT max(id) FROM order_id);")
        order_id = self.cursor.fetchone()
        self.assertEqual(get_data.get_order_id(db_config.db_conf['name']),
                         order_id)

    def test_delete_order_id(self):
        self.cursor.execute("SELECT * FROM order_id WHERE \
                              id=(SELECT max(id) FROM order_id);")
        order_id = self.cursor.fetchone()
        get_data.delete_order_id(db_config.db_conf['name'])
        self.cursor.execute("SELECT * FROM order_id WHERE \
                              id=(SELECT max(id) FROM order_id);")
        order_id1 = self.cursor.fetchone()
        self.assertNotEqual(order_id, order_id1)

    def test_delete_order(self):
        self.cursor.execute("SELECT * FROM CreateOrder WHERE \
                              id=(SELECT max(id) FROM CreateOrder);")
        order = self.cursor.fetchone()
        get_data.delete_order(db_config.db_conf['name'])
        self.cursor.execute("SELECT * FROM CreateOrder WHERE \
                              id=(SELECT max(id) FROM CreateOrder);")
        order_after_delete = self.cursor.fetchone()
        self.assertNotEqual(order, order_after_delete)

    def test_for_get_data(self):
        self.cursor.execute("SELECT * FROM phone_number WHERE \
                            id=(SELECT max(id) FROM phone_number);")
        phone_number1 = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM fare WHERE \
                             id=(SELECT max(id) FROM fare);")
        fare = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM address WHERE \
                             id=(SELECT max(id) FROM address);")
        address = self.cursor.fetchone()
        print(address)
        self.assertNotEqual(get_data.get_data(db_config.db_conf['name']),
                            phone_number1, fare)
