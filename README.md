# Gestion des employés — Django

Application Django de gestion des employés (CRUD complet) avec connexion et compte de démonstration. Projet d'Emile Dufoulon ; les données sont fictives.

**En ligne :** https://gestion-employes.vercel.app/ (bouton « Essayer la démo — sans compte »)

## Fonctionnalités

- Liste, ajout, modification et suppression d'employés (nom, e-mail, poste, salaire)
- Validation des formulaires avec messages d'erreur (e-mail valide, salaire positif)
- Accès réservé aux utilisateurs connectés ; compte démo en un clic, données de démo restaurables
- Administration Django (`/admin/`)
- Tests automatisés (`python manage.py test`)

## Stack

Python · Django 6 · PostgreSQL (Neon) en production, SQLite en local · DaisyUI / Tailwind (CDN) · WhiteNoise · Vercel

## Lancer en local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_DEBUG=1          # mode développement, base SQLite locale
python manage.py migrate
python manage.py createsuperuser   # facultatif, pour /admin/
python manage.py runserver
python manage.py test
```

## Variables d'environnement (production, Vercel)

| Variable | Rôle |
|---|---|
| `DJANGO_SECRET_KEY` | clé secrète longue et aléatoire (obligatoire) |
| `DATABASE_URL` | adresse de connexion PostgreSQL Neon (`postgresql://…?sslmode=require`) |
| `DJANGO_ALLOWED_HOSTS` | facultatif, par défaut `.vercel.app,localhost,127.0.0.1` |
| `DJANGO_DEBUG` | ne pas définir en production |

Les migrations sont appliquées automatiquement au démarrage de la fonction Vercel (`api/index.py`).
Pour créer un administrateur sur Neon : `DATABASE_URL=… DJANGO_SECRET_KEY=… python manage.py createsuperuser` depuis ta machine.
