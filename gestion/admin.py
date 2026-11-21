from django.contrib import admin

from .models import Employe


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'poste', 'salaire')
    search_fields = ('nom', 'email', 'poste')
