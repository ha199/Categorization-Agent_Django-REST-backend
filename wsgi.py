import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

if not settings.configured:
    settings.configure(
        DEBUG=True,
        INSTALLED_APPS=['rest_framework'],
        MIDDLEWARE=[],
        ROOT_URLCONF='urls',
    )

django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
