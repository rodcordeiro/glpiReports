import logging
import os,platform
from decouple import config
import json

import datetime


from glpi import GLPI
from zabbix import zabbix
from reports import reports

logger = logging.getLogger("ReportTools")
logging.basicConfig(level=logging.INFO)

class app:
    def __init__(self):
      logger.info(f"Initializing ReportTools session")
      self.zabbix = zabbix()
      self.glpi = GLPI()
      self.reports = reports(self)
    
    def close(self):
      self.glpi.session.killSession()
      logger.info(f"Closing session.")
      


    

# 
# 
# 
# 
# 
# 
# 

app = app()
app.reports.get_client_hosts()
app.close()
