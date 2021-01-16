import os,platform
from decouple import config
import json

from App import APP

from Controllers.Tickets import ticketController
from Controllers.Users import userController
from Controllers.Reports import Reports

app = APP().start()

# report = Reports(app)


