import requests
import json
from decouple import config

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

    def getTickets(self):
        """
        Filter can be initialized from filters factory or by simply creating instance of this class.

        Examples:

        .. code-block:: python

            @dp.message_handler(commands=['myCommand'])
            @dp.message_handler(Command(['myCommand']))
            @dp.message_handler(commands=['myCommand'], commands_prefix='!/')

        :param commands: Command or list of commands always without leading slashes (prefix)
        :param prefixes: Allowed commands prefix. By default is slash.
            If you change the default behavior pass the list of prefixes to this argument.
        :param ignore_case: Ignore case of the command
        :param ignore_mention: Ignore mention in command
            (By default this filter pass only the commands addressed to current bot)
        :param ignore_caption: Ignore caption from message (in message types like photo, video, audio, etc)
            By default is True. If you want check commands in captions, you also should set required content_types.

            Examples:

            .. code-block:: python

                @dp.message_handler(commands=['myCommand'], commands_ignore_caption=False, content_types=ContentType.ANY)
                @dp.message_handler(Command(['myCommand'], ignore_caption=False), content_types=[ContentType.TEXT, ContentType.DOCUMENT])
        """
        url = config("BASE_URL") + "/Ticket"
        querystring = {
            "Content-Type":"application/json",
            "app_token":self.app_token,
            "session_token":self.session_token,
            "range":"0-99999",
            "order":"DESC"
            }
        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        return response.text
    
    

