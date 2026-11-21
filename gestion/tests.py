from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .demo import DEMO_EMPLOYES
from .models import Employe


class AccesTests(TestCase):
    def test_liste_redirige_vers_connexion_si_anonyme(self):
        response = self.client.get(reverse('liste_employes'))
        self.assertRedirects(response, f"{reverse('connexion')}?next=/")

    def test_bouton_demo_connecte_et_cree_les_donnees(self):
        response = self.client.post(reverse('connexion_demo'))
        self.assertRedirects(response, reverse('liste_employes'))
        self.assertEqual(Employe.objects.count(), len(DEMO_EMPLOYES))
        self.assertContains(self.client.get(reverse('liste_employes')), DEMO_EMPLOYES[0]['nom'])

    def test_demo_refuse_le_get(self):
        self.assertEqual(self.client.get(reverse('connexion_demo')).status_code, 405)


class CrudTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user('test', password='mot-de-passe-solide-42')
        self.client.force_login(user)

    def test_ajout_valide(self):
        response = self.client.post(reverse('ajouter_employe'), {
            'nom': 'Alice Durand', 'email': 'alice@exemple.fr', 'poste': 'Développeuse', 'salaire': '2800.00',
        })
        self.assertRedirects(response, reverse('liste_employes'))
        self.assertEqual(Employe.objects.get().nom, 'Alice Durand')

    def test_ajout_invalide_affiche_les_erreurs(self):
        response = self.client.post(reverse('ajouter_employe'), {
            'nom': '', 'email': 'pas-un-email', 'poste': 'Dev', 'salaire': '-5',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employe.objects.count(), 0)
        self.assertTrue(response.context['form'].errors)

    def test_recherche_et_chiffres_cles(self):
        Employe.objects.create(nom='Alice Durand', email='alice@exemple.fr', poste='Développeuse', salaire=Decimal('3000'))
        Employe.objects.create(nom='Bob Martin', email='bob@exemple.fr', poste='Support', salaire=Decimal('2000'))
        response = self.client.get(reverse('liste_employes'), {'q': 'support'})
        self.assertEqual([e.nom for e in response.context['employes']], ['Bob Martin'])
        self.assertEqual(response.context['stats']['effectif'], 2)
        self.assertEqual(response.context['stats']['masse'], Decimal('5000'))
        self.assertEqual(response.context['stats']['moyenne'], Decimal('2500'))

    def test_erreur_reliee_au_champ(self):
        response = self.client.post(reverse('ajouter_employe'), {'nom': '', 'email': 'x', 'poste': 'Dev', 'salaire': '1'})
        self.assertContains(response, 'aria-invalid="true"')
        self.assertContains(response, 'id="id_email-error"')

    def test_modification_et_suppression(self):
        emp = Employe.objects.create(nom='Bob', email='bob@exemple.fr', poste='Support', salaire=Decimal('2000'))
        self.client.post(reverse('modifier_employe', args=[emp.id]), {
            'nom': 'Bob Martin', 'email': 'bob@exemple.fr', 'poste': 'Support', 'salaire': '2100',
        })
        emp.refresh_from_db()
        self.assertEqual(emp.nom, 'Bob Martin')
        self.assertEqual(str(emp), 'Bob Martin')

        self.client.post(reverse('supprimer_employe', args=[emp.id]))
        self.assertFalse(Employe.objects.exists())
