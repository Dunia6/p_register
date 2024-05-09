from django.contrib import admin
from .models import Frais, TypesFrais
# Register your models here.


class FraisAdmin(admin.ModelAdmin):
    """ Affichage des Informations complètes sur le frais d'un étudiant dans l'interface Admin du site """
    list_display = ('etudiant', 'designation', 'montant_payer', 'lieu_paiement', 'agent')


admin.site.register(TypesFrais)
admin.site.register(Frais, FraisAdmin)
