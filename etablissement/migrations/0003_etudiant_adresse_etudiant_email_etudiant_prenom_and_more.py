# Generated by Django 4.0.6 on 2024-05-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etablissement', '0002_rename_stucture_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='adresse',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='prenom',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='telephone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
