from django.db import models

# Create your models here.
class TypesFrais(models.Model):
    """ Modèle Types de frais """
    designation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.designation

class Frais(models.Model):
    """ Modèle des frais """
    etudiant = models.ForeignKey('etablissement.Etudiant', on_delete=models.CASCADE, default=None)
    designation = models.ForeignKey(TypesFrais, on_delete=models.CASCADE)
    montant_payer = models.FloatField(default=0.0)
    lieu_paiement = models.CharField(max_length=50, default="")
    en_ordre = models.BooleanField()
    registered_at = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.designation