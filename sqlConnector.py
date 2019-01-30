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



def getLatest(url):
    try:
        conn = connect()
        cursor = conn.cursor()
        queryComp = "SELECT LATEST FROM manga WHERE name = %s"
        name = (url,)
        cursor.execute(queryComp,name)
        temp = cursor.fetchone()
    except Error as e:
        print('Error:',e)
    finally:
        if temp != None:
            return temp[0]
        else:
            return None
        cursor.close()
        conn.close()    
    


def update(name,url,latest):
    try:
        conn = connect()
        cursor = conn.cursor()
        queryUpdate = "INSERT INTO manga (name,url,latest) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE latest=%s"
        args = (name, url, latest, latest)
        cursor.execute(queryUpdate,args)
        conn.commit()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    connect()
