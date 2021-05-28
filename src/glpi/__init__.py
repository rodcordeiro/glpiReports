import logging
import requests
import json
from decouple import config

from .controllers.Session import session
from .controllers.User import user

logger = logging.getLogger(__name__)

class GLPI:
    def __init__(self):
        self.app_token = config("GLPI_APPTOKEN")
        self.session = session(self.app_token)
        self.session_token = self.session.session_token
        self.user = user(self)
        self.techs = self.user.getTechs()
        self.clients = self.user.getClients()
        logger.info("GLPI plugin connected")
