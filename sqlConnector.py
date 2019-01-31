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
        query = "SELECT latest FROM manga WHERE name = %s"
        name = (url,)
        cursor.execute(query,name)
        temp = cursor.fetchone()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()    
        if temp != None:
            return temp[0]
        else:
            return None
    


def update(name,url,latest,numPages):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "INSERT INTO manga (name,url,latest,numPages,crawled) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE latest=%s"
        args = (name, url, latest, numPages, 0, latest)
        cursor.execute(query,args)
        conn.commit()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()

def getMangaNames():
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT name FROM manga"
        cursor.execute(query)
        names = cursor.fetchall()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()
        return names

def getMangaPage(name):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT numPages FROM manga WHERE name=%s"
        args = (name,)
        cursor.execute(query,args)
        page = cursor.fetchone()[0]
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"+page)
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()
        return page

def updateMangaPage(name,totalPage):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "UPDATE manga SET numPages = %s WHERE name = %s"
        args = (totalPage,name)
        cursor.execute(query,args)
        conn.commit()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()


def getCrawled(name):
    try:
	status = 0
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT crawled FROM manga WHERE name=%s"
        args = (name,)
        cursor.execute(query,args)
        status = cursor.fetchone()[0]
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()
        return status


def updateCrawled(name,status):
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "UPDATE manga SET crawled = %s WHERE name = %s"
        args = (status,name)
        cursor.execute(query,args)
        conn.commit()
    except Error as e:
        print('Error:',e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    connect()

