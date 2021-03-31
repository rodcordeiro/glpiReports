import requests
import json
from decouple import config

class session:
    def __init__(self,app_token):
        self.app_token = app_token
        self.session_token = ''
        self.createSession()
    
    def createSession(self):
        url = config("GLPI_BASEURL") + "/initSession"
        headers={"Content-Type":"application/json","App-Token":self.app_token,"Authorization":"user_token {}".format(config("GLPI_USERTOKEN"))}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            token = response.json().get("session_token")
            self.session_token = token
        else:
            print("Falha ao iniciar sessão no GLPI: ",response.text)
            return exit(0)

    
    def killSession(self):
        url = config("GLPI_BASEURL") + "/killSession"
        headers = {"Content-Type":"application/json","App-Token":self.app_token,"Session-Token": self.session_token}
        payload = ""
        response = requests.get(url, data=payload, headers = headers)
        print(response)
        return response.status_code
    
    def getProfiles(self):
        url = config("GLPI_BASEURL") + "/getMyProfiles"
        querystring = {"Content-Type":"application/json","app_token":self.app_token,"session_token":self.session_token}
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        return response.json()
    
    