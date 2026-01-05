import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "gestion_perso.settings"
)

app = get_wsgi_application()
