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
    
    def close(self):
      self.glpi.session.killSession()

    def teste(self):
      host = self.zabbix.get_client_hosts("Globom")
      for h in host:
        print(h['name'])

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

app.close()
print("finished")