from django.core.validators import MinValueValidator
from django.db import models


class Employe(models.Model):
    nom = models.CharField(max_length=80)
    email = models.EmailField()
    poste = models.CharField(max_length=80)
    salaire = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Salaire mensuel brut en euros",
    )

    class Meta:
        ordering = ['nom']
        verbose_name = 'employé'

    def __str__(self):
        return self.nom

    @property
    def initiales(self):
        return "".join(mot[0] for mot in self.nom.split()[:2]).upper()
