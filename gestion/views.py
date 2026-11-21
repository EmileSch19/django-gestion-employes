from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .demo import get_demo_user, reset_demo_data
from .forms import EmployeForm
from .models import Employe


@login_required
def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employe/list.html', {'employes': employes})


@login_required
def ajouter_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        employe = form.save()
        messages.success(request, f"{employe.nom} a été ajouté.")
        return redirect('liste_employes')
    return render(request, 'employe/formulaire.html', {'form': form, 'titre': 'Ajouter un employé'})


@login_required
def modifier_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        messages.success(request, f"{employe.nom} a été modifié.")
        return redirect('liste_employes')
    return render(request, 'employe/formulaire.html', {'form': form, 'titre': f'Modifier {employe.nom}'})


@login_required
def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == "POST":
        nom = employe.nom
        employe.delete()
        messages.success(request, f"{nom} a été supprimé.")
        return redirect('liste_employes')
    return render(request, 'employe/confirmation_suppression.html', {'emp': employe})


@require_POST
def connexion_demo(request):
    """Connecte le visiteur au compte démo (sans mot de passe)."""
    login(request, get_demo_user(), backend='django.contrib.auth.backends.ModelBackend')
    if not Employe.objects.exists():
        reset_demo_data()
    return redirect('liste_employes')


@login_required
@require_POST
def reinitialiser_demo(request):
    reset_demo_data()
    messages.success(request, "Les données de démonstration ont été restaurées.")
    return redirect('liste_employes')
