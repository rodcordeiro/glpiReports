import requests
import json
from decouple import config

class userController:
    def __init__(self,app_token,session_token):
        self.app_token = app_token
        self.session_token = session_token

    def getClients(self):
        url = config("BASE_URL") + "/search/User/"
        querystring = {
            "Content-Type":"application/json",
            "app_token":self.app_token,
            "session_token":self.session_token,
            "range":"0-200",
            "order":"ASC",
            "criteria[0][itemtype]":"User",
            "criteria[0][field]":"13",
            "criteria[0][searchtype]":"contains",
            "criteria[0][value]":"Clientes",
            "forcedisplay[0]":["1","2"]
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        return response.text
    
