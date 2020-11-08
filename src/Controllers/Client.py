import json
import datetime

class Client:
    def __init__(self,id,name,tickets):
        self.__init__= self
        self.id = id
        self.name = name
        self.tickets = tickets
        self.preventiva = 0
        self.corretiva = 0
        self.remoto = 0
        self.tempo_preventiva = 0
        self.tempo_corretiva = 0
        self.tempo_remoto = 0
        self.calculaPreventiva()
        # self.calculaCorretiva()
        # self.calculaRemoto()
    
    def calculaPreventiva(self):
        # if self.tickets:
        print(self.id)
        print(self.name)
        print(self.tickets)
        
        # if self.tickets != None:
        #     for ticket in self.tickets:
        #         if ticket['7'] == "Preventiva":
        #             self.preventiva += 1
        #             if ticket['45'] and ticket['45'] != 0:
        #                 self.tempo_preventiva += ticket['45']
        #             elif ticket['45'] and ticket['45'] == 0:
        #                 time = datetime.datetime.strptime(ticket['19'], "%m-%d-%Y %H:%M:%S").date() - datetime.datetime.strptime(ticket['15'], "%m-%d-%Y %H:%M:%S").date()
        #                 self.tempo_preventiva += time
        return self

    def calculaCorretiva(self):
            for ticket in self.tickets:
                if ticket['7'] == "Corretiva":
                    self.corretiva += 1
                    if ticket['45'] and ticket['45'] != 0:
                        self.tempo_corretiva += ticket['45']
                    elif ticket['45'] and ticket['45'] == 0:
                        time = datetime.datetime.strptime(ticket['19'], "%m-%d-%Y %H:%M:%S").date() - datetime.datetime.strptime(ticket['15'], "%m-%d-%Y %H:%M:%S").date()
                        self.tempo_corretiva += time
            return self

    def calculaRemoto(self):
            for ticket in self.tickets:
                if ticket['7'] == "Remoto":
                    self.remoto += 1
                    if ticket['45'] and ticket['45'] != 0:
                        self.tempo_remoto += ticket['45']
                    elif ticket['45'] and ticket['45'] == 0:
                        time = datetime.datetime.strptime(ticket['19'], "%m-%d-%Y %H:%M:%S").date() - datetime.datetime.strptime(ticket['15'], "%m-%d-%Y %H:%M:%S").date()
                        self.tempo_remoto += time
            return self
