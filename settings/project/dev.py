"""
development mode specific project settings
"""
from settings.dev import *

INSTALLED_APPS += (
    'teracy.html5boilerplate',
    'apps.hello',
    'apps.polls',
)