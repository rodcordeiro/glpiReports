import os,platform
import json
from decouple import config

from Controllers.Session import sessionController

class APP:
    """
    Instantiate the app object
    """
    def __init__(self):
        self.app_token = config("LINK_TIM_TOKEN")
        self.session_token = sessionController(self.app_token).createSession()

    def getPubAdd(self):
        response = os.popen("wget -qO - ipv4.icanhazip.com").readlines()[0].split('\n')[0]
        return response

    def getToken(self,link):
        if link == config("LINK_TIM_IP"):
            return config("LINK_TIM_TOKEN")
        elif link == config("LINK_VIVO_IP"):
            return config("LINK_VIVO_TOKEN")
        else:
            print("Invalid external IP Address")
            exit()
    