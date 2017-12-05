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






















