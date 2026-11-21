from django import forms
from .models import Employe


class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'email', 'poste', 'salaire']
        labels = {
            'nom': 'Nom',
            'email': 'E-mail',
            'poste': 'Poste',
            'salaire': 'Salaire mensuel brut (€)',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'input w-full', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'input w-full', 'autocomplete': 'email'}),
            'poste': forms.TextInput(attrs={'class': 'input w-full'}),
            'salaire': forms.NumberInput(attrs={'class': 'input w-full', 'min': '0', 'step': '0.01'}),
        }
