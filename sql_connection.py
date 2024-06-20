import mysql.connector
__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Soumya@123',
                                  host='127.0.0.1',
                                  database='gswebapp')
    return __cnx