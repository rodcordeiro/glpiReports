import os,platform
import json
from decouple import config

from Controllers.Session import sessionController

class APP:
    """
    Instantiate the app object
    """
    def __init__(self):
        self.app_token = ""
        self.session_token = ""

    def start(self):
        self.app_token = config("LOCAL_TOKEN")
        self.session_token = self.getToken()
        return self

    def getToken(self):
        token = sessionController(self.app_token).createSession()
        if token == False:
            self.app_token == config("LINK_VIVO_TOKEN") if self.app_token == config("LINK_TIM_TOKEN") else config("LINK_TIM_TOKEN")
            self.getToken()
        return token