# Generated by Django 4.0.6 on 2024-05-09 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frais',
            name='agent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
