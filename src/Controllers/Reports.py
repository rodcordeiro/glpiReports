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
        self.technicians = self.users.getTechs()["data"]
    
    def getClients(self):
        clients = self.users.getClients()["data"]
        data = {}
        i = 0
        # for client in clients:
        #     data[client['2']]={}
        #     data[client['2']]["name"]=client['1']
        #     data[client['2']]["tickets"]=self.getTikets(client['2'])
        #     i += 1
        for client in clients:
            print(client['1'])
            data[client['2']]=Client(client['2'],client['1'],self.getTikets(client['2']))
            # print(data[client['2']].id)
            # print(data[client['2']].name)
            # print(data[client['2']].tickets)
            # print(data[client['2']].preventiva)
            # print(data[client['2']].corretiva)
            # print(data[client['2']].remoto)
            # print(data[client['2']].tempo_preventiva)
            # print(data[client['2']].tempo_corretiva)
            # print(data[client['2']].tempo_remoto)
            
            i += 1
        
        return data
    
    def getTikets(self,client):
        tickets = self.tickets.getTicketsLastMonth(client)
        return tickets
