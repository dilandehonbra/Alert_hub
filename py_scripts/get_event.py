import mysql.connector
from mysql.connector import errorcode
import json
import sys

UserName = "zabbix"
Password = "ls32bits"
RemoteHost = "localhost"
MySQLPort = int(3306)
DatabaseName = "zabbix"

def getEvents():
    try:
        conn = mysql.connector.connect(
            user=UserName,
            password=Password,
            host=RemoteHost,
            port=MySQLPort,
            database=DatabaseName
        )
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT * FROM zabbix.events")
        cursor.execute(query)

        results = []
        for row in cursor:
            results.append(row)
        cursor.close()
        conn.close()
        return json.dumps(results, indent=4)

    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")

        else:
            print(err)