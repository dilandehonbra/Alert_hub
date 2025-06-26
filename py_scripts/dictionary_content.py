import mysql.connector
from mysql.connector import errorcode
import sys
import json
sys.path.append('/home/ubuntu/alert_hub/py_scripts')
import get_event

# Variáveis de conexão Banco
UserName = "alerthub"
Password = "alerthub"
RemoteHost = "localhost"
MySQLPort = int(33006)
DatabaseName = "alert_hub_zabbix"

def insertEventsAlerthub(
        eventid, source, object_, objectid,
        clock, value, acknowledged, ns,
        name, severity
):
    try:
        conn = mysql.connector.connect(
            user=UserName,
            password=Password,
            host=RemoteHost,
            port=MySQLPort,
            database=DatabaseName
        )
        cursor = conn.cursor()

        query = """
                INSERT INTO zabbix_events (
                    eventid, source, object, objectid,
                    clock, value, acknowledged, ns,
                    name, severity
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        data = (
            eventid, source, object_, objectid,
            clock, value, acknowledged, ns,
            name, severity
        )
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return False

events_json = get_event.getEvents()
events_dic = json.loads(events_json)

for i in events_dic:
    insertEventsAlerthub(
        i.get('eventid'),
        i.get('source'),
        i.get('object'),
        i.get('objectid'),
        i.get('clock'),
        i.get('value'),
        i.get('acknowledged'),
        i.get('ns'),
        i.get('name'),
        i.get('severity')
    )