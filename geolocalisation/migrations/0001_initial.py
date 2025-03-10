# Generated by Django 5.0.6 on 2024-07-22 21:39

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Chauffeur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('permis', models.FileField(upload_to='documents/')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chauffeurs', to='geolocalisation.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marque', models.CharField(max_length=100)),
                ('modèle', models.CharField(max_length=100)),
                ('position', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voitures', to='geolocalisation.admin')),
                ('chauffeur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='voiture', to='geolocalisation.chauffeur')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geolocalisation.voiture')),
            ],
        ),
        migrations.CreateModel(
            name='Commander',
            fields=[
                ('idcomd', models.AutoField(primary_key=True, serialize=False)),
                ('datecomd', models.DateTimeField()),
                ('destination', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('devise', models.CharField(max_length=10)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('statut', models.CharField(default='En attente', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='geolocalisation.client')),
                ('voiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='geolocalisation.voiture')),
            ],
        ),
    ]
