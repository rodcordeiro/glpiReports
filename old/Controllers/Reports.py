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
        self.users = app.user
        self.tickets = app.ticket
        
    def report(self):
        self.getClients()
        for client in self.clients:
            print(self.clients[client].name)
            self.clients[client].tickets = self.getTickets(self.clients[client].id)
            self.clients[client].preventiva = 0
            self.clients[client].corretiva = 0
            self.clients[client].remoto = 0
            self.clients[client].origins = {
            "Direct" : 0,
            "E-mail" : 0,
            "Helpdesk": 0,
            "Other": 0,
            "Phone": 0,
            "Whatsapp": 0,
            "Written": 0
        }
            self.clients[client].tempo_presencial = 0
            self.clients[client].tempo_remoto = 0
            if self.clients[client].tickets != None:
                for ticket in self.clients[client].tickets:
                    if ticket['7'] == "Preventiva":
                        self.clients[client].preventiva += 1
                        if ticket['45'] and ticket['45'] != 0:
                            self.clients[client].tempo_presencial += ticket['45']
                        else:
                            if ticket['45'] and ticket['45'] == 0:
                                time = datetime.datetime.strptime(ticket['19'], "%m-%d-%Y %H:%M:%S").date() - datetime.datetime.strptime(ticket['15'], "%m-%d-%Y %H:%M:%S").date()
                                self.clients[client].tempo_presencial += time
                    elif ticket['7'] == "Corretiva":
                        self.clients[client].corretiva += 1
                        if ticket['45'] and ticket['45'] != 0:
                            self.clients[client].tempo_presencial += ticket['45']
                        else:
                            if ticket['45'] and ticket['45'] == 0:
                                time = datetime.datetime.strptime(ticket['19'], "%m-%d-%Y %H:%M:%S").date() - datetime.datetime.strptime(ticket['15'], "%m-%d-%Y %H:%M:%S").date()
                                self.clients[client].tempo_presencial += time
                    elif ticket['7'] == "Remoto":
                        self.clients[client].remoto += 1
                        if ticket['45'] and ticket['45'] != 0:
                            self.clients[client].tempo_remoto += ticket['45']
                        elif ticket['45'] and ticket['45'] == 0:
                            time = datetime.datetime.strptime(ticket['19'], "%m-%d-%Y %H:%M:%S").date() - datetime.datetime.strptime(ticket['15'], "%m-%d-%Y %H:%M:%S").date()
                            self.clients[client].tempo_remoto += time
                if self.clients[client].origins[ticket['9']]:
                    self.clients[client].origins[ticket['9']] = self.clients[client].origins[ticket['9']]+1
                else:
                    self.clients[client].origins[ticket['9']] = 1
            print(self.clients[client].tickets)
            print(self.clients[client].origins)
            print(self.clients[client].preventiva)
            print(self.clients[client].corretiva)
            print(self.clients[client].remoto)
            print(self.clients[client].tempo_presencial)
            print(self.clients[client].tempo_remoto)
        


    def getClients(self):
        clients = self.users.getClients()
        data = {}
        for client in clients:
            data[client['2']]=Client(client['2'],client['1'])
        self.clients = data
    
    def getTickets(self,client):
        tickets = self.tickets.getTicketsReport(client)
        tech = self.users.getTechs()
        if tickets:
            for ticket in tickets:
                try:
                    ticket['5'] = tech[ticket['5']]
                except:
                    ticket['5'] = "Analista não encontrado"
            return tickets
        else:
            return None