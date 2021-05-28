import logging
import requests
import json
from decouple import config
from pyzabbix import ZabbixAPI

logger = logging.getLogger(__name__)

class zabbix:
    """
    Instantiate the Zabbix object
    """
    def __init__(self):
        self.zabbix = ZabbixAPI(config('ZABBIX_HOST'))
        self.zabbix.login(user=config('ZABBIX_USER'),password=config('ZABBIX_PWD'))
        self.session = self.zabbix.check_authentication()
        self.hosts = self.zabbix.host.get({"output":"extend"})
        logger.info("Zabbix plugin connected")
        
        

    def getHosts(self):
        response = []
        for host in self.hosts:
            response.append(host['name'])
        return response
    
    def getHost(self):
        host = [self.hosts[2],self.hosts[4],self.hosts[10]]
        # host['items'] = self.zabbix.item.get({"output":"extend","select_triggers":"extend","hostids":[host['hostid']]})
        return host

    def get_client_hosts(self,client):
        search={
            "output": "extend", 
            "search": {
                "name": [
                    f"{client}*"
                ]
            },
            "searchWildcardsEnabled":1
        }
        response = self.zabbix.do_request('host.get',search)
        for host in response['result']:
            host['backups'] = self.get_host_backup(host['hostid'])
        return response['result']
    
    def get_host_backup(self,hostid):
        items = self.zabbix.item.get({
            "output": "extend",
            "select_triggers":"extend",
            "hostids":[hostid]
        })
        response = {
            "totalItems":0,
            "successful":{
                "id":False,
                "items":''
            },
            "failed":{
                "id":False,
                "items":''
            }
            
            }
        for item in items:
            if item['name'] == "Windows Backup Trouble":
                if item['hostid'] == hostid:
                    response['failed']['id'] = item['itemid']
                    response['failed']['items'] = item
                    response['totalItems'] += 1
            elif item['name'] == "Windows Backup Successful":
                if item['hostid'] == hostid:
                    response['successful']['id'] = item['itemid']
                    response['successful']['items'] = item
                    response['totalItems'] += 1

        if response['failed']['id']:
            response['failed']['history'] = self.zabbix.do_request('history.get',{
                "output": "extend",
                "itemids":[response['failed']['id']],
                "sortfield": "clock",
            })
        if response['successful']['id']:
            response['successful']['history'] = self.zabbix.do_request('history.get',{
                "output": "extend",
                "itemids":[response['successful']['id']],
                "history": 4,
                "sortfield": "clock",
            })
        return response
