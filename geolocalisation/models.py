# Importation des modules nécessaires
from django.contrib.gis.db import models as gis_models
from django.db import models

# Définition du modèle Admin
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

# Définition du modèle Chauffeur
class Chauffeur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    permis = models.FileField(upload_to='documents/')
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='chauffeurs')

    def __str__(self):
        return self.nom

# Définition du modèle Voiture
class Voiture(models.Model):
    id = models.AutoField(primary_key=True)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    position = gis_models.PointField(geography=True, srid=4326, null=True, blank=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='voitures')
    chauffeur = models.OneToOneField(Chauffeur, on_delete=models.CASCADE, related_name='voiture')

    def obtenir_position(self):
        return self.position

    def __str__(self):
        return f"{self.marque} {self.modele}"

# Définition du modèle Client
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

# Définition du modèle Commander
class Commander(models.Model):

    DEVISE_CHOICES = [
        ('USD', 'Dollar américain'),
        ('CDF', 'Franc congolais'),
        ('EUR', 'Euro'),
    ]
    idcomd = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes')
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name='commandes')
    datecomd = models.DateTimeField()
    destination = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    devise = models.CharField(max_length=3, choices=DEVISE_CHOICES, default='USD')
    commentaire = models.TextField(null=True, blank=True)
    statut = models.CharField(max_length=50, default='En attente')

    def __str__(self):
        return f"Commande {self.idcomd} par {self.client.nom} pour {self.voiture.marque} {self.voiture.modele} à destination de {self.destination}"

# Définition du modèle Location
class Location(models.Model):
    vehicule = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = gis_models.PointField(geography=True, srid=4326, null=True, blank=True)

    def __str__(self):
        return f"Location de {self.vehicule} à {self.timestamp}"




class Conduire(models.Model):
    id = models.AutoField(primary_key=True)
    date_prise = models.DateTimeField()
    etat = models.CharField(max_length=100)
    chauffeur = models.ForeignKey(Chauffeur, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.chauffeur.nom} conduit {self.voiture.marque} {self.voiture.modèle} le {self.date_prise}"