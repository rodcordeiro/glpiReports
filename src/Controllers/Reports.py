import requests
import json
from decouple import config

from .Tickets import ticketController
from .Users import userController

class Reports:
    '''
    Instantiate the app to control all process involving tickets
    '''
    def __init__(self,app):
        """
        Instantiate the app to control all process involving tickets
        :param app: The object that has the App instance.
        """
        self.app = app
        self.users = userController(app)
        self.tickets = ticketController(app)
        self.clients = self.getClients()
        self.technicians = self.users.getTechs()["data"]
    
    def getClients(self):
        clients = self.users.getClients()["data"]
        data = {}
        i = 0
        for client in clients:
            data[client['2']]={}
            data[client['2']]["name"]=client['1']
            data[client['2']]["tickets"]=self.getTikets(client['2'])
            i += 1
        return data
    
    def getTikets(self,client):
        tickets = self.tickets.getTicketsLastMonth(client)
        return tickets
