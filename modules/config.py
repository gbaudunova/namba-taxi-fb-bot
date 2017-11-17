import sqlite3


def insertPhoneNumbers(data):
    db = sqlite3.connect('./phone_numbers.db')
    c = db.cursor()
    #c.execute("CREATE TABLE contacts (Numbers INTEGER)")
    variable = data['entry'][0]['messaging'][0]['message']['text']
    print(variable)
    c.execute("INSERT INTO contacts VALUES (?)", (variable, ))
    db.commit()













    # print(variable)
    # with sqlite3.connect('../phone_numbers.db') as db:
    #     c = db.cursor()
    #     sql = "create table contacts (numbers)"
    #     sql = "insert into contacts (variable) values (?)"
    #     c.execute(sql)
    #     db.commit()



















 # #   #c.execute("CREATE TABLE phone(numbers integer)")
 #     c.execute("INSERT INTO phone VALUES (?)", (variable,))
 #    #      #print(c.fetchall())
 #     #conn.commit()
 #    # c.execute("SELECT * FROM phone WHERE numbers='+996700080577'")
 #    conn.close()


    #     conn = sqlite3.connect('../phone_numbers.db')
    #     c = conn.cursor()
    # # #   #c.execute("CREATE TABLE phone(numbers integer)")
    # #     c.execute("INSERT INTO phone VALUES (?)", (variable,))
    # #     #print(c.fetchall())
    # #     #conn.commit()
    # #     # c.execute("SELECT * FROM phone WHERE numbers='+996700080577'")
    #     conn.close()