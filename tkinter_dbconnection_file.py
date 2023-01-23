from logging import exception
# from sqlite3 import Cursor
from mysql.connector.cursor import MySQLCursor

class mysqlCon:
    conn = ""

    def __init__(self):  # self represents the instance of the class. Usage of "self" in class to access the methods and attributes
        #    The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes
        print("Hello, this is as an initializer method of class mysqlCon ...")

    def fndbconn():
        global conn
        # We import the connector class from MySql.
        import mysql.connector as mysqlConnector
        conn = mysqlConnector.connect(
            host='localhost', user='root', password='sagar@123', database='testdb')  # We access the connect method through the connector class, which we already import into our program. Now, we are passing our connection parameters to the connect method. The user name and password will be different according to your installation process.
        if conn:
            return 1
        else:
            return 0

    def fnLogin(tmpuser, tmppass):
        global conn
        # We imported the cursor method from the established connection (conn) object and created the cursor object (mycursor).
        mycursor = conn.cursor()

        print(f"Entered Username = {tmpuser}")
        print(f"Entered Password = {tmppass}")

        tuple1 = (tmpuser, tmppass)

        query = """select * from users where username=%s and password=%s"""
        # we use %s for character code as ASCII 65 is 'A' so till 91 'Z' to understand better you can use for loop starting from 65 to 91 inside this for loop print result using printf
        # The execute () method helps us to execute the query and return records according to the query.
        result = mycursor.execute(query, tuple1)
        # Returns the all or remaining rows from the result set.
        result = mycursor.fetchone()
        print(f"Result = {result}")

        return result

        # conn.close()

    def fnRegister(username, password, tmpemailid):
        mycursor = conn.cursor()
        print(username, password, tmpemailid)
        mycursor.execute(
            f"insert into users(username,password,email_id) values('{username}','{password}','{tmpemailid}')")
        conn.commit()
        conn.close()
