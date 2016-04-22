"""
WSGI config for azurecasts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from os.path import join, dirname, abspath
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Accesses .env file in parent directory.
dotenv_path = join(abspath('.'), '.env')
load_dotenv(dotenv_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azurecasts.settings")

application = get_wsgi_application()
