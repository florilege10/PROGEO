from rest_framework import serializers
from .models import Chauffeur, Client, Commander, Voiture, Conduire

# Serializers pour les opérations de liste
class ChauffeurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = ['id', 'nom']  # Limiter aux champs nécessaires pour la liste

class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nom']  # Limiter aux champs nécessaires pour la liste

class CommanderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        fields = ['idcomd', 'client', 'voiture', 'datecomd', 'destination']  # Limiter aux champs nécessaires pour la liste

class VoitureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ['id', 'marque', 'modèle']  # Limiter aux champs nécessaires pour la liste

class ConduireListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conduire
        fields = ['id', 'date_prise', 'etat', 'chauffeur', 'voiture']  # Limiter aux champs nécessaires pour la liste

# Serializers pour les opérations de détail
class ChauffeurDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chauffeur
        fields = '__all__'

class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CommanderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        fields = '__all__'

class VoitureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'

class ConduireDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conduire
        fields = '__all__'
