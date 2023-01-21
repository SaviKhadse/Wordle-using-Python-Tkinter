from logging import exception
from sqlite3 import Cursor


class mysqlCon:
    conn = ""

    def __init__(self):
        print("Hello, this is class mysqlCon from file testdbfile...")

    def fndbconn():
        global conn
        import mysql.connector as mysqlConnector
        conn = mysqlConnector.connect(
            host='localhost', user='root', password='rootroot1234', database='PythonWordle')
        if conn:
            return 1
        else:
            return 0

    def fnLogin(tmpuser, tmppass):
        global conn
        mycursor = conn.cursor()

        print(f"Entered Username = {tmpuser}")
        print(f"Entered Password = {tmppass}")

        tuple1 = (tmpuser, tmppass)

        query = """select * from users1 where username=%s and password=%s"""

        result = mycursor.execute(query, tuple1)
        result = mycursor.fetchall()
        print(f"Result = {result}")

        return result
        # conn.close()

    def fnRegister(username, password, tmpemailid):
        mycursor = conn.cursor()
        print(username, password, tmpemailid)
        mycursor.execute(
            f"insert into users1(username,password,email_id) values('{username}','{password}','{tmpemailid}')")
        conn.commit()
        conn.close()
