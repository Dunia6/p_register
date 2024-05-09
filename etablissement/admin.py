from django.contrib import admin
from .models import Etudiant, Departement, Promotion, Structure, AnneeAcademique


from django.utils.translation import gettext_lazy as _
# Register your models here.

class StructureAdmin(admin.ModelAdmin):
    raw_id_fields = ('annee_academique',)

class PromotionAdmin(admin.ModelAdmin):
    raw_id_fields = ('departement',)

class DepartementAdmin(admin.ModelAdmin):
    raw_id_fields = ('structure',)

class EtudiantAdmin(admin.ModelAdmin):
    """ Affichage desInformations complètes sur un étudiant dans l'interface Admin du site """
    list_display = ('full_name', 'promotion', 'departement', 'structure', 'created_at')
    # list_filter = ('promotion', 'created_at')
    list_filter = ('promotion__departement__structure__name', 'promotion__departement__name',)
    raw_id_fields = ('promotion',)
    
    @admin.display(description='Departement')
    def departement(self, obj):
        return obj.promotion.departement.name

    @admin.display(description='Structure')
    def structure(self, obj):
        return obj.promotion.departement.structure.name


admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Structure, StructureAdmin)
admin.site.register(AnneeAcademique)


admin.site.site_header = _('ESI Payement register Administration')