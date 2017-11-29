import sqlite3
from api.requests import create_order


def get_data():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM phone_number WHERE id=(SELECT max(id) FROM phone_number);")
    phone_number = c.fetchone()
    print(phone_number[1])
    c.execute("SELECT * FROM fare WHERE id=(SELECT max(id) FROM fare);")
    fare = c.fetchone()
    print(fare[1])
    c.execute("SELECT * FROM address WHERE id=(SELECT max(id) FROM address);")
    address = c.fetchone()
    print(address[1])
    db.commit()
    create_order(phone_number, fare, address)























