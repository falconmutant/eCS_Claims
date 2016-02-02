"""
WSGI config for ecsclaims project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecsclaims.settings")


import sys
import traceback
import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import base64
import mimetypes
from email.mime.text import MIMEText
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'client_gmail.json'
APPLICATION_NAME = 'Gmail API Python'
credential_dir = os.path.join(home_dir, '.credentials')
if  os.path.exists(credential_dir):
	credential_path = os.path.join(credential_dir,'gmail-python-quickstart.json')
    #store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if credentials and not credentials.invalid:
    	http = credentials.authorize(httplib2.Http())
    	from django.conf import settings
      	settings.SERVICE_GMAIL = discovery.build('gmail', 'v1', http=http)

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
