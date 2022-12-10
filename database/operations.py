from flask_mysqldb import MySQL, MySQLdb

mysql = MySQL()


# Read DB
def execute_read_query(query):
    cursor = mysql.connection.cursor()
    result = None
    try:
        cursor.execute(query)
        if cursor.rowcount == 1:
            result = cursor.fetchone()
            result = [result]

        else:
            result = cursor.fetchall()
        return result
    except MySQLdb.OperationalError as e:
        print(f'MySQL server has gone away: {e}, trying to reconnect')
        raise e


# Write DB
def execute_query(query):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(query)
        mysql.connection.commit()

        ID = cursor.lastrowid
        cursor.close()
        return ID
    except MySQLdb.OperationalError as e:
        print(f'MySQL server has gone away: {e}, trying to reconnect')
        raise e
