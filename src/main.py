import os,platform
from decouple import config

from app import APP

from Controllers.Tickets import ticketController
from Controllers.Users import userController

app = APP()

# USERS = userController(APP_TOKEN,SESSION.session_token)

TICKET = ticketController(app)
tickets = TICKET.getTickets()

print(tickets)
