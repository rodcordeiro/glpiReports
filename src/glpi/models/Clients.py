import json
import datetime

class Client:
    def __init__(self,id,name,tickets = [], hosts = []):
        self.id = id
        self.name = name
        self.tickets = tickets
        self.hosts = hosts
        self.preventiva = 0
        self.corretiva = 0
        self.remoto = 0
        self.tempo_presencial = 0
        self.tempo_remoto = 0