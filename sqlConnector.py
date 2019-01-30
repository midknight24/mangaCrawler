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
    try:
        conn = connect()
        cursor = conn.cursor()
        queryComp = "SELECT LATEST FROM manga WHERE name = %s"
        cursor.execute(queryComp,name)
        temp = cursor.fetchone();
        if temp != None:
            return temp[0]
        else:
            return None
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()    
    


def update(name,url):
    try:
        conn = connect()
        cursor = conn.cursor
        queryUpdate = "INSERT INTO MANGA (name,latest) VALUES (%s,%s) ON DUPLICATE KEY UPDATE latest=%s"
        args = (name, url, url)
        cursor.execute(queryUpdate,args)
        conn.commit()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    connect()