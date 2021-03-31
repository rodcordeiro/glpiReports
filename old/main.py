import os,platform
from decouple import config
import json

import datetime


from App import APP

app = APP()
print("""====================================
  START APP:
------------------------------------
app_token: {}
session_token: {}
====================================""".format(app.app_token,app.session_token))

app.teste()