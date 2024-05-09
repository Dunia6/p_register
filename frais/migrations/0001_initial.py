# Generated by Django 4.0.6 on 2024-05-03 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etablissement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='', max_length=50)),
                ('type_frais', models.CharField(choices=[('Frais tout étudiant', 'Frais tout étudiant'), ('Frais par département', 'Frais par département'), ('Frais pour finalistes', 'Frais pour finalistes'), ('Frais pour une promotion', 'Frais pour une promotion')], default='', max_length=50)),
                ('montant_a_payer', models.FloatField()),
                ('montant_payer', models.FloatField(default=0.0)),
                ('lieu_paiement', models.CharField(default='', max_length=50)),
                ('registered_at', models.DateField(default='')),
                ('en_ordre', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etablissement.etudiant')),
            ],
        ),
    ]