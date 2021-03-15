import requests
import json
from decouple import config
import datetime

class ticketController:
    '''
    Instantiate the app to control all process involving tickets
    '''
    def __init__(self,app):
        """
        Instantiate the app to control all process involving tickets
        :param app: The object that has the App instance.
        """
        self.app_token = app.app_token
        self.session_token = app.session_token

    def getAllTickets(self):
        """
        Returns all tickets.

        Examples:

        .. code-block:: python

            getAllTickets()
        """

        url = config("BASE_URL") + "/Ticket"
        headers = {"Content-Type":"application/json","App-Token":self.app_token,"Session-Token": self.session_token}
        querystring = {
            "range":"0-999999",
            "order":"DESC"
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring, headers = headers)
        return response.json()
    
    def getTicket(self,id):
        """
        Returns the ticket

        Examples:

        .. code-block:: python

            getTicket(13)

        :param id: ID to be used for filtering the requester of the tickets.
        """

        url = config("BASE_URL") + "/Ticket/{}".format(id)
        headers = {"Content-Type":"application/json","App-Token":self.app_token,"Session-Token": self.session_token}
        querystring = {
            "range":"0-999999",
            "order":"DESC"
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring, headers = headers)
        return response.json()
        
    def getTicketsReport(self,id):
        """
        Returns the last month tickets, if :id is provided it filters for the user.

        Examples:

        .. code-block:: python

            getTicketsLastMonth(13)

        :param id: ID to be used for filtering the requester of the tickets.
        """
        url = config("BASE_URL") + "/search/Ticket/"
        headers = {"Content-Type":"application/json","App-Token":self.app_token,"Session-Token": self.session_token}
        date = getThisMonth()
        querystring = {
            "range":"0-99999",
            "order":"DESC",
            "criteria[0][itemtype]": "Ticket",
            "criteria[0][field]": "15",
            "criteria[0][searchtype]": "morethan",
            "criteria[0][value]": datetime.datetime.strftime(date["init"],"%Y-%m-%d %H:%M:%S"),
            "criteria[1][link]": "AND",
            "criteria[1][itemtype]": "Ticket",
            "criteria[1][field]": "15",
            "criteria[1][searchtype]": "lessthan",
            "criteria[1][value]": datetime.datetime.strftime(date["end"],"%Y-%m-%d %H:%M:%S"),
            "criteria[2][link]": "AND",
            "criteria[2][itemtype]": "Ticket",
            "criteria[2][searchtype]": "equals",
            "criteria[2][value]": id,
            "criteria[2][field]": "4",
            "forcedisplay[0]": "1",
            "forcedisplay[1]": "2",
            "forcedisplay[2]": "12",
            "forcedisplay[3]": "15",
            "forcedisplay[4]": "19",
            "forcedisplay[5]": "3",
            "forcedisplay[6]": "4",
            "forcedisplay[7]": "5",
            "forcedisplay[8]": "7",
            "forcedisplay[9]": "45",
            "forcedisplay[10]": "36",
            "forcedisplay[11]": "9"
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring,headers = headers)
        return response.json().get("data")

def getThisMonth():
    date = datetime.date.today()
    if date.month == 1:
        monthInit = 12 
        yearInit = date.year - 1
    else:
        monthInit = date.month - 1
        yearInit = date.year
    init = "{}-{}-{} 00:00:00".format(monthInit, "01",yearInit)
    end = "{}-{}-{} 00:00:00".format(date.month, "01",date.year)
    date = {
        "init":datetime.datetime.strptime(init, "%m-%d-%Y %H:%M:%S").date(),
        "end":datetime.datetime.strptime(end, "%m-%d-%Y %H:%M:%S").date()
        }
    return date


            