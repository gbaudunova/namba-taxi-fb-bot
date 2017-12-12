import sqlite3


def insert_phone_numbers(data):
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    variable = data['entry'][0]['messaging'][0]['message']['text']
    c.execute("INSERT INTO phone_number VALUES (NULL, ?)", (variable,))
    db.commit()


def insert_fares(data):
    db1 = sqlite3.connect('NambaTaxiBot.db')
    conn = db1.cursor()
    callback = data['entry'][0]['messaging'][0]['postback']['payload']
    conn.execute("INSERT INTO fare VALUES (NULL, ?)", (callback,))
    db1.commit()


def insert_address(data):
    db2 = sqlite3.connect('NambaTaxiBot.db')
    conn1 = db2.cursor()
    address = data['entry'][0]['messaging'][0]['message']['text']
    conn1.execute("INSERT INTO address VALUES (NULL, ?)", (address,))
    db2.commit()
