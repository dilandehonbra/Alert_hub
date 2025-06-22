import mysql.connector
from mysql.connector import errorcode
import json
import sys

UserName = "alerthub"
Password = "alerthub"
RemoteHost = "localhost"
MySQLPort = int(33006)
DatabaseName = "alerthub"

try:
    conn = mysql.connector.connect(
        user=UserName,
        password=Password,
        host=RemoteHost,
        port=MySQLPort,
        database=DatabaseName
    )
    cursor = conn.cursor(dictionary=True)
    query = ("SELECT * FROM teste")
    cursor.execute(query)


    for row in cursor:
        print(json.dumps(row, indent=4))
    cursor.close()
    conn.close()

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")

    else:
        print(err)
