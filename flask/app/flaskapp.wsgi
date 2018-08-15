#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/srv/udacity_project/flask/app')

from app import app as application

application.secret_key = 'super_secret_key'  # This needs changing in production env
