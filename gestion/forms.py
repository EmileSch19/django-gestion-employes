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
            'nom': forms.TextInput(attrs={'class': 'field', 'autocomplete': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'field', 'autocomplete': 'email'}),
            'poste': forms.TextInput(attrs={'class': 'field'}),
            'salaire': forms.NumberInput(attrs={'class': 'field', 'min': '0', 'step': '0.01'}),
        }

    def full_clean(self):
        super().full_clean()
        # Relie chaque champ en erreur à son message (lecteurs d'écran)
        for name in self.errors:
            if name in self.fields:
                self.fields[name].widget.attrs.update({
                    'aria-invalid': 'true',
                    'aria-describedby': f'id_{name}-error',
                })
