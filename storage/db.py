import sqlite3


def insert_phone_numbers(data, db_name):
    db = sqlite3.connect(db_name)
    c = db.cursor()
    variable = data['entry'][0]['messaging'][0]['message']['text']
    c.execute("INSERT INTO phone_number VALUES (NULL, ?)", (variable,))
    db.commit()


def insert_fares(data, db_name):
    db1 = sqlite3.connect(db_name)
    conn = db1.cursor()
    callback = data['entry'][0]['messaging'][0]['postback']['payload']
    conn.execute("INSERT INTO fare VALUES (NULL, ?)", (callback,))
    db1.commit()


def insert_address(data, db_name):
    db2 = sqlite3.connect(db_name)
    conn1 = db2.cursor()
    address = data['entry'][0]['messaging'][0]['message']['text']
    conn1.execute("INSERT INTO address VALUES (NULL, ?)", (address,))
    db2.commit()


def insert_data_creation_order(db_name):
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
    c.execute("SELECT * FROM order_id WHERE "
              "id=(SELECT max(id) FROM order_id);")
    order_id = c.fetchone()
    c.execute("INSERT INTO CreateOrder (phonenumber, fare, address,"
              " order_id) VALUES (?, ?, ?, ?)",
              (str(phone_number[1]), str(fare[1]), str(address[1]),
               str(order_id[1]),))
    db.commit()
