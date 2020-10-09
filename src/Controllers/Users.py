import requests
import json
from decouple import config


class userController:
    '''
    Controller that holds all process involving users.
    '''
    def __init__(self,app):
        """
        Instantiate the app to control all process involving users
        :param app: The object that has the App instance.
        """
        self.app_token = app.app_token
        self.session_token = app.session_token

    def getClients(self):
        url = config("BASE_URL") + "/search/User/"
        querystring = {
            "Content-Type":"application/json",
            "app_token":self.app_token,
            "session_token":self.session_token,
            "range":"0-100",
            "order":"ASC",
            "criteria[0][itemtype]":"User",
            "criteria[0][field]":"13",
            "criteria[0][searchtype]":"contains",
            "criteria[0][value]":"Clientes",
            "forcedisplay[0]":["1","2"]
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        return response.json()
        
    def getTechs(self):
        url = config("BASE_URL") + "/search/User/"
        querystring = {
            "Content-Type":"application/json",
            "app_token":self.app_token,
            "session_token":self.session_token,
            "range":"0-100",
            "order":"ASC",
            "criteria[0][itemtype]":"User",
            "criteria[0][field]":"13",
            "criteria[0][searchtype]":"contains",
            "criteria[0][value]":"Área técnica"
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        return response.json()
