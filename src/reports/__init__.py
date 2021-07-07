import logging
import requests
import json
from decouple import config

logger = logging.getLogger(__name__)

class reports:
    def __init__(self,app):
        self.glpi = app.glpi
        self.zabbix = app.zabbix
        logger.info("Reports plugin connected")
    
    def get_client_hosts(self):
        self.clients = self.glpi.clients
        for client in self.clients:
            client.hosts = self.zabbix.get_client_hosts(client.name)
            print(client.name,client.hosts)

    def teste(self):
        response = self.zabbix.get_host_backup(10369)
        print(response)
        for item in response['items']:
            print(item)
    
    def create_report(self,ReportFile):
        logger.info(f"Creating report on {ReportFile}")
        f = open(ReportFile, "a")
        f.write(str(self.glpi.clients))
        f.close()

        



            