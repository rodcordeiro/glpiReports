import json
import datetime

class Client:
    def __init__(self,id,name,tickets = [], hosts = []):
        self.__init__= self
        self.id = id
        self.name = name
        self.tickets = tickets
        self.hosts = hosts
