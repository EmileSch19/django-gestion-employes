from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.liste_employes, name="liste_employes"),
    path("ajouter/", views.ajouter_employe, name="ajouter_employe"),
    path("modifier/<int:id>/", views.modifier_employe, name="modifier_employe"),
    path("supprimer/<int:id>/", views.supprimer_employe, name="supprimer_employe"),
    path(
        "connexion/",
        auth_views.LoginView.as_view(template_name="employe/connexion.html", redirect_authenticated_user=True),
        name="connexion",
    ),
    path("deconnexion/", auth_views.LogoutView.as_view(), name="deconnexion"),
    path("demo/", views.connexion_demo, name="connexion_demo"),
    path("demo/reinitialiser/", views.reinitialiser_demo, name="reinitialiser_demo"),
]
