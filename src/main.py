import os,platform
from decouple import config
import json

import datetime


from glpi import GLPI
from zabbix import zabbix
from reports import reports

print("started")

class app:
    def __init__(self):
      self.glpi = GLPI()
      self.zabbix = zabbix()
      self.reports = reports(self)
    
    def teste(self):
      host=self.zabbix.get_client_hosts("Fercab")
      backupSuccess=''
      backupError=''
      agentAvailability=''
      # for item in host['items']:
      #   if item['name'] == "Windiws Backup Trouble":
      #     backupSuccess = item
      #   elif item['name'] == "Windows Backup Successful":
      #     backupError = item
      #   elif item['name'] == "Zabbix agent availability":
      #     agentAvailability = item
      for h in host:
        print(h['name'])
      # print(backupSuccess)
      # print(backupError)
      # print(agentAvailability)
# 
# Windiws Backup Trouble
# Windows Backup Successful
# Zabbix agent availability
# 
# 
# 
# 
# 
# 

app = app()
app.teste()
print("finished")