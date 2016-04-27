from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse

from jinja2 import Environment

from compressor.contrib.jinja2ext import CompressorExtension

from azurecasts import settings


def environment(**options):
    """
    Function used as a callable in settings.py when configuring the Jinja2
    backend. Adds static() and url() helpers for user in templates along with
    configuring an extension for django-compressor.
    :param options:
    :return env: Jinja2 environment.
    """
    options['extensions'] = [CompressorExtension]
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env