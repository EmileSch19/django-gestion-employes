"""Données de démonstration (fictives) et compte démo."""

from decimal import Decimal

from django.contrib.auth import get_user_model

from .models import Employe

DEMO_USERNAME = 'demo'

DEMO_EMPLOYES = [
    {'nom': 'Camille Martin', 'email': 'camille.martin@exemple.fr', 'poste': 'Développeuse back-end', 'salaire': Decimal('3200.00')},
    {'nom': 'Hugo Bernard', 'email': 'hugo.bernard@exemple.fr', 'poste': 'Administrateur réseau', 'salaire': Decimal('2900.00')},
    {'nom': 'Inès Petit', 'email': 'ines.petit@exemple.fr', 'poste': 'Cheffe de projet', 'salaire': Decimal('3600.00')},
    {'nom': 'Lucas Robert', 'email': 'lucas.robert@exemple.fr', 'poste': 'Technicien support', 'salaire': Decimal('2200.00')},
]


def get_demo_user():
    user, created = get_user_model().objects.get_or_create(username=DEMO_USERNAME)
    if created:
        # Pas de mot de passe : on ne se connecte au compte démo que par le bouton
        user.set_unusable_password()
        user.save()
    return user


def reset_demo_data():
    Employe.objects.all().delete()
    Employe.objects.bulk_create(Employe(**e) for e in DEMO_EMPLOYES)
