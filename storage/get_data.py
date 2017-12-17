import sqlite3


def get_data():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM phone_number WHERE "
              "id=(SELECT max(id) FROM phone_number);")
    phone_number = c.fetchone()
    c.execute("SELECT * FROM fare WHERE "
              "id=(SELECT max(id) FROM fare);")
    fare = c.fetchone()
    c.execute("SELECT * FROM address WHERE "
              "id=(SELECT max(id) FROM address);")
    address = c.fetchone()
    db.commit()
    return phone_number, fare, address


def get_data_creation_order():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM phone_number WHERE "
              "id=(SELECT max(id) FROM phone_number);")
    phone_number = c.fetchone()
    c.execute("SELECT * FROM fare WHERE "
              "id=(SELECT max(id) FROM fare);")
    fare = c.fetchone()
    c.execute("SELECT * FROM address WHERE "
              "id=(SELECT max(id) FROM address);")
    address = c.fetchone()
    c.execute("SELECT * FROM order_id WHERE "
              "id=(SELECT max(id) FROM order_id);")
    order_id = c.fetchone()
    c.execute("INSERT INTO CreateOrder (phonenumber, fare, address,"
              " order_id) VALUES (?, ?, ?, ?)",
              (str(phone_number[1]), str(fare[1]), str(address[1]),
               str(order_id[1]),))
    db.commit()


def delete_order():
    db4 = sqlite3.connect('NambaTaxiBot.db')
    conn3 = db4.cursor()
    conn3.execute('DELETE FROM CreateOrder WHERE '
                  'id=(SELECT max(id) FROM CreateOrder);')
    db4.commit()


def get_order_id():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM order_id WHERE "
              "id=(SELECT max(id) FROM order_id);")
    order_id = c.fetchone()
    db.commit()
    return order_id


def get_address():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM address WHERE "
              "id=(SELECT max(id) FROM address);")
    address_data = c.fetchone()
    db.commit()
    return address_data
