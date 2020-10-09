import requests
import json
from decouple import config

class sessionController:
    def __init__(self,app_token):
        self.app_token = app_token
        self.session_token = ''
    
    def createSession(self):
        url = config("BASE_URL") + "/initSession"
        querystring = {"Content-Type":"application/json","app_token":self.app_token,"login":config("USERNAME"),"password":config("PASSWORD")}
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        if response.status_code == 200:
            token = response.json().get("session_token")
            self.session_token = token
            return token
        else:
            return False

    
    def killSession(self):
        url = config("BASE_URL") + "/killSession"
        querystring = {"Content-Type":"application/json","app_token":self.app_token,"session_token":self.session_token}
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        print(response)
        return response.status_code
    
    def getProfiles(self):
        url = config("BASE_URL") + "/getMyProfiles"
        querystring = {"Content-Type":"application/json","app_token":self.app_token,"session_token":self.session_token}
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        return response.json()
    
    