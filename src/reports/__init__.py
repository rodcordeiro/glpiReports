import requests
import json
from decouple import config

class reports:
    def __init__(self,app):
        self.glpi = app.glpi
        self.zabbix = app.zabbix