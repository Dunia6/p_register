from django.shortcuts import render, redirect, get_object_or_404
from . models import Frais
from .forms import FraisForm

from etablissement.models import Etudiant
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def Creer_frais(request, id):
    """ Vue créer frais """
    etudiant = get_object_or_404(Etudiant, pk=id)
    decisiom = ""
    message = ""
    double_frais = ""
    
    
    form = FraisForm()
    if request.method == 'POST':
        form = FraisForm(request.POST)
        if form.is_valid():
            frais = form.save(commit=False)
            frais.etudiant = etudiant
            
            for etudiant in etudiant.frais_set.all():
                if frais.designation == etudiant.designation:
                    decisiom = 1
                    messages.error(request, "Ce Frais a déjà été enregistré !")
                    double_frais = 1
                    break
                
            
            if double_frais != 1:
                frais.save()
                decisiom = 0
                message = "Frais enregistré avec succes !"
            return redirect('detail_etudiant', id=id)
        context = {'form': form, 'decision': decisiom, 'message': message, 'etudiant': etudiant}
        return render(request, 'frais/creer_frais.html', context)
    else:
        form = FraisForm()
        context = {'form': form, 'decision': decisiom, 'message': message, 'etudiant': etudiant}
        return render(request, 'frais/creer_frais.html', context)
