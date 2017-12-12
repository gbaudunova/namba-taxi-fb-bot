import sqlite3


def get_data():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM phone_number WHERE id=(SELECT max(id) FROM phone_number);")
    phone_number = c.fetchone()
    c.execute("SELECT * FROM fare WHERE id=(SELECT max(id) FROM fare);")
    fare = c.fetchone()
    c.execute("SELECT * FROM address WHERE id=(SELECT max(id) FROM address);")
    address = c.fetchone()
    db.commit()
    return phone_number, fare, address


def get_order_id():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM order_id WHERE id=(SELECT max(id) FROM order_id);")
    order_id = c.fetchone()
    db.commit()
    return order_id


def get_address():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM address WHERE id=(SELECT max(id) FROM address);")
    address_data = c.fetchone()
    db.commit()
    return address_data
