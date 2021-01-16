import requests
import json
from decouple import config

from .Tickets import ticketController
from .Users import userController
from .Client import Client

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
        

    def getClients(self):
        clients = self.users.getClients()["data"]
        data = {}
        i = 0
        for client in clients:
            data[client['2']]=Client(client['2'],client['1'],self.getTikets(client['2']))
            i += 1
        return data
    
    def getTikets(self,client):
        tickets = self.tickets.getTicketsLastMonth(client)
        tech = self.users.getTechs()
        if tickets:
            for ticket in tickets:
                ticket['5'] = tech[ticket['5']]
                print(ticket)
            return tickets
        else:
            return None
