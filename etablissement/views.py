from django.shortcuts import render, get_object_or_404
from . models import Etudiant, Departement, Promotion, Structure, AnneeAcademique
from django.contrib.auth.decorators import login_required
# from frais.models import Frais

from django.contrib import messages
# Create your views here.

@login_required(login_url="login")
def home(request):
    """ Vue de la page d'accueil """
    annee_academiques = AnneeAcademique.objects.filter(active=True)
    structures = Structure.objects.all()
    departements = Departement.objects.all()
    promotions = Promotion.objects.all()
    etudiants = Etudiant.objects.all()
    
    context = {
        'annee_academiques': annee_academiques,
        'structures': structures,
        'departements': departements,
        'promotions': promotions,
        'etudiants': etudiants
    }
    return render(request, 'etablissement/home.html', context)


@login_required(login_url="login")
def etudiant_detail(request, id):
    """ Vue de la page detail étudiant """
    mes_messages = messages.get_messages(request)
    
    etudiant = get_object_or_404(Etudiant, pk=id)
    promotion = etudiant.promotion
    departement = promotion.departement
    structure = departement.structure
    annee_academique = structure.annee_academique
    frais = etudiant.frais_set.all()
    
    context = {

        "etudiant" : etudiant,
        "promotion" : promotion,
        "departement" : departement,
        "structure" : structure,
        "annee_academique" : annee_academique,
        "frais" : frais,
        "mes_messages" : mes_messages
    }
    
    return render(request, "etudiant/detail_etudiant.html", context)