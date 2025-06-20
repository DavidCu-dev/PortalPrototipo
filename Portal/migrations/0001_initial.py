# Generated by Django 5.2.3 on 2025-06-17 00:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='datosGenerales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=255)),
                ('email', models.EmailField(default='from@example.com', max_length=255)),
                ('rfc', models.CharField(max_length=13)),
                ('telefono', models.CharField(max_length=30)),
                ('razonSocial', models.CharField(max_length=255)),
                ('giro', models.CharField(max_length=255)),
                ('domicilio', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
