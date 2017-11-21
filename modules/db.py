import sqlite3


def insertPhoneNumbers(data):
    db = sqlite3.connect('./phone_numbers.db')
    c = db.cursor()
    #c.execute("CREATE TABLE contacts (Numbers INTEGER)")
    variable = data['entry'][0]['messaging'][0]['message']['text']
    print(variable)
    c.execute("INSERT INTO contacts VALUES (?)", (variable, ))
    db.commit()

























