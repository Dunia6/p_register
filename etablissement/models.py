from django.db import models

""" importer uuid """
import uuid

# Create your models here.


class AnneeAcademique(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("AnneeAcademique")
        verbose_name_plural = ("AnneesAcademiques")
        ordering = ['name']

    def __str__(self):
        return self.name


class Structure(models.Model):
    name = models.CharField(max_length=50)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Stucture")
        verbose_name_plural = ("Stuctures")
        ordering = ['name']

    def __str__(self):
        return self.name


class Departement(models.Model):
    name = models.CharField(max_length=50)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Departement")
        verbose_name_plural = ("Departements")
        ordering = ['name']

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=50)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    est_finale = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Promotion")
        verbose_name_plural = ("Promotions")
        ordering = ['name']

    def __str__(self):
        return self.name



class Etudiant(models.Model):
    SEXE = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, null=True, blank=True)
    adresse = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    sexe = models.CharField(max_length=1, choices=SEXE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Etudiant")
        verbose_name_plural = ("Etudiants")
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name} - {self.promotion}"