import requests
import json
import getpass

ZABBIX_API_URL = "http://192.168.1.155/zabbix/api_jsonrpc.php"

def loginZabbixApi(userName=None, userPass=None):

    if userName is None:
        userName = input("User: ")
    if userPass is None:
        userPass = getpass.getpass("Password: ")

    r = requests.post(ZABBIX_API_URL,
                      json={
                          "jsonrpc": "2.0",
                          "method": "user.login",
                          "params": {
                              "username": userName,
                              "password": userPass
                          },
                          "id": 1
                      })

    loginResponse = r.json()

    if 'result' in loginResponse:
        return loginResponse['result']
    else:
        raise Exception(f"Login failed: {loginResponse.get('error', {}).get('data', 'Unknown error')}")

def logout(authToken):
    r = requests.post(ZABBIX_API_URL,
                      json={
                          "jsonrpc": "2.0",
                          "method": "user.logout",
                          "params": {},
                          "id": 2,
                          "auth": authToken
                      })
    logoutResponse = r.json()

    if logoutResponse.get('result') == True:
        return True
    else:
        raise Exception(f"Logout failed: {logoutResponse.get('error', {}).get('data', 'Unknown error')}")
