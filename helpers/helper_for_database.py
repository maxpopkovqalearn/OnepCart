import mysql.connector

def getDBQuery(query_for_sql):
    try:
        connection = mysql.connector.connect(
            user='root',
            password='password',
            host='127.0.0.1',
            port='3306',
            database='storedb')
        cursor = connection.cursor()
        cursor.execute(query_for_sql)
        result = cursor.fetchall()

        return result

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))