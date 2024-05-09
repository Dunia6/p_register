from django import forms
from .models import Frais



class FraisForm(forms.ModelForm):
    class Meta:
        model = Frais
        fields = ['designation', 'montant_payer', 'lieu_paiement', 'en_ordre']
        widgets = {
            'designation': forms.Select(attrs={'class': 'form-control', 'placeholder': "Entrez la désignation"}),
            'montant_payer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Entrez le montant"}),
            'lieu_paiement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entrez le lieu"}),
            'en_ordre': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': True}),
        }
        labels = {
            'designation': 'Désignation du frais',
            'montant_payer': 'Montant à payer:',
            'lieu_paiement': 'Lieu de paiement',
            'en_ordre': 'Paiement en ordre',
        }


