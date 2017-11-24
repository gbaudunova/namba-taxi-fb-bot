import sqlite3
import uuid


def CreateOrder():
    db = sqlite3.connect('NambaTaxiBot.db')
    c = db.cursor()
    # c.execute("SELECT last_insert_rowid() FROM phoneNumbers")
    # c.execute("SELECT max(Numbers) FROM phoneNumbers")
    c.execute("SELECT * FROM phoneNumbers WHERE id=(SELECT max(id) FROM phoneNumbers);")
    phoneNumber = c.fetchone()
    print(phoneNumber)
    c.execute("SELECT * FROM Fares WHERE id=(SELECT max(id) FROM Fares);")
    fare = c.fetchone()
    print(fare)
    c.execute("SELECT * FROM Address WHERE id=(SELECT max(id) FROM Address);")
    address = c.fetchone()
    orderId = str(uuid.uuid4().fields[0])[:8]
    print(address)
    c.execute("INSERT INTO CreateOrder (phoneNumber, fare, address, orderId) VALUES (?, ?, ?, ?)", (str(phoneNumber[1]), str(fare[1]), str(address[1]), orderId, ))
    db.commit()

# print(str(uuid.uuid4().fields[0])[:8])