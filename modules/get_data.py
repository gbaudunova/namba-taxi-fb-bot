import sqlite3


def get_data():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    c.execute("SELECT * FROM phoneNumbers WHERE id=(SELECT max(id) FROM phoneNumbers);")
    PHONE_NUMBER = c.fetchone()
    return PHONE_NUMBER
    c.execute("SELECT * FROM Fares WHERE id=(SELECT max(id) FROM Fares);")
    FARE = c.fetchone()
    return FARE
    c.execute("SELECT * FROM Address WHERE id=(SELECT max(id) FROM Address);")
    ADDRESS = c.fetchone()
    return ADDRESS
    db.commit()
    create_order(phone_number, fare, address)



















# def CreateOrder():
#     db = sqlite3.connect('NambaTaxiBot.db')
#     c = db.cursor()
#     c.execute("SELECT * FROM phoneNumbers WHERE id=(SELECT max(id) FROM phoneNumbers);")
#     phoneNumber = c.fetchone()
#     print(phoneNumber)
#     c.execute("SELECT * FROM Fares WHERE id=(SELECT max(id) FROM Fares);")
#     fare = c.fetchone()
#     print(fare)
#     c.execute("SELECT * FROM Address WHERE id=(SELECT max(id) FROM Address);")
#     address = c.fetchone()
#     orderId = str(uuid.uuid4().fields[0])[:8]
#     print(address)
#     c.execute("INSERT INTO CreateOrder (phoneNumber, fare, address, orderId) VALUES (?, ?, ?, ?)", (str(phoneNumber[1]), str(fare[1]), str(address[1]), orderId, ))
#     db.commit()

