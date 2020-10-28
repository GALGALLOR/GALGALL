import mysql.connector

mydb =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="GALGALLO10",
    db="aliebrain")
cursor = mydb.cursor()
names = input('state your names ')


def if_not_init():
    cursor.execute('INSERT INTO user(names) VALUES ("' + names + '")')
    mydb.commit()
    print('now its there')

def if_in():
    cursor.execute('SELECT FROM user WHERE names = "'+names+'"')
    f = cursor.fetchall()
    for x in f:
        if names in x:
            print('it was and has been there')
        else:
            if_not_init()
