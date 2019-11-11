import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="testing"
)

cursor = con.cursor()


def user_login(tup):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `username`=%s AND `password`=%s", tup)
        return (cursor.fetchone())
    except:
        return False