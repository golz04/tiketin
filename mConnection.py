import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tiketin'
    )

if db.is_connected():
    print("databse is connected")
else:
    print("connection error")

global cursor
cursor = db.cursor()

