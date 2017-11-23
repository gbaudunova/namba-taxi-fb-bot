import sqlite3


def insertPhoneNumbers(data):
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    #c.execute("CREATE TABLE phoneNumbers (id INTEGER PRIMARY KEY AUTOINCREMENT, Numbers INTEGER)")
    variable = data['entry'][0]['messaging'][0]['message']['text']
    c.execute("INSERT INTO phoneNumbers VALUES (NULL, ?)", (variable,))
    db.commit()


def insertFares(data):
    db1 = sqlite3.connect('NambaTaxiBot.db')
    conn = db1.cursor()
    #conn.execute("CREATE TABLE Fares (id INTEGER PRIMARY KEY AUTOINCREMENT, fares TEXT)")
    callback = data['entry'][0]['messaging'][0]['postback']['payload']
    conn.execute("INSERT INTO Fares VALUES (NULL, ?)", (callback,))
    db1.commit()


def insertAddress(data):
    db2 = sqlite3.connect('NambaTaxiBot.db')
    conn1 = db2.cursor()
    #conn1.execute("CREATE TABLE Address (id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT)")
    address = data['entry'][0]['messaging'][0]['message']['text']
    conn1.execute("INSERT INTO Address VALUES (NULL, ?)", (address,))
    db2.commit()





#









    # db.close()
    # c.close()
