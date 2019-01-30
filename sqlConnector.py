import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='127.0.0.1',
                                       database='mangaList',
                                       user='root',
                                       password='admin')
        if conn.is_connected():
            print('Connected to MySQL database')

        return conn
 
    except Error as e:
        print(e)

def getLatest(name):
    conn = connect()
    cursor = conn.cursor()
    queryComp = "SELECT LATEST FROM manga WHERE name = %s"
    cursor.execute(queryComp,name)
    temp = cursor.fetchone();
    if(temp != None):
        return temp[0]
 
if __name__ == '__main__':
    connect()