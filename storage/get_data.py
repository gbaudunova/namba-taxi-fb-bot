import sqlite3


def get_data(db_name):
    db = sqlite3.connect(db_name)
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


def delete_order(db_name):
    db4 = sqlite3.connect(db_name)
    conn3 = db4.cursor()
    conn3.execute('DELETE FROM CreateOrder WHERE '
                  'id=(SELECT max(id) FROM CreateOrder);')
    db4.commit()


def get_order_id(db_name):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute("SELECT * FROM order_id WHERE "
              "id=(SELECT max(id) FROM order_id);")
    order_id = c.fetchone()
    db.commit()
    return order_id


def delete_order_id(db_name):
    db4 = sqlite3.connect(db_name)
    conn3 = db4.cursor()
    conn3.execute('DELETE FROM order_id WHERE '
                  'id=(SELECT max(id) FROM order_id);')
    db4.commit()


def get_address(db_name):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    c.execute("SELECT * FROM address WHERE "
              "id=(SELECT max(id) FROM address);")
    address_data = c.fetchone()
    db.commit()
    return address_data
