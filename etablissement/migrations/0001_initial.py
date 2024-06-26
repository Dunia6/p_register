# Generated by Django 4.0.6 on 2024-05-09 09:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeAcademique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'AnneeAcademique',
                'verbose_name_plural': 'AnneesAcademiques',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Departement',
                'verbose_name_plural': 'Departements',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('annee_academique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.anneeacademique')),
            ],
            options={
                'verbose_name': 'Stucture',
                'verbose_name_plural': 'Stuctures',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('est_finale', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.departement')),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('lieu_de_naissance', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.promotion')),
            ],
            options={
                'verbose_name': 'Etudiant',
                'verbose_name_plural': 'Etudiants',
                'ordering': ['full_name'],
            },
        ),
        migrations.AddField(
            model_name='departement',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.structure'),
        ),
    ]
