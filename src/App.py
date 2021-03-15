import os,platform
import json
from decouple import config

from Controllers.Session import sessionController
from Controllers.Tickets import ticketController
from Controllers.Users import userController
from Controllers.Reports import Reports

class APP:
    """
    Instantiate the app object
    """
    def __init__(self):
        self.app_token = config("APP_TOKEN")
        self.session = sessionController(self.app_token)
        self.session_token = self.session.session_token
        self.ticket = ticketController(self)
        self.user = userController(self)
        self.reports = Reports(self)
    
    def teste(self):
        self.reports.report()