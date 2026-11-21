import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestion_perso.settings")

app = get_wsgi_application()

# Applique les migrations au démarrage de la fonction Vercel (sans effet si la base est à jour)
from django.core.management import call_command  # noqa: E402

call_command("migrate", interactive=False, verbosity=0)
