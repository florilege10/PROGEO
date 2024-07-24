from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import *
from .models import Chauffeur, Client, Commander, Voiture, Conduire
from .serializers import (
    ChauffeurListSerializer, ChauffeurDetailSerializer,
    ClientListSerializer, ClientDetailSerializer,
    CommanderListSerializer, CommanderDetailSerializer,
    VoitureListSerializer, VoitureDetailSerializer,
    ConduireListSerializer, ConduireDetailSerializer
)




class ChauffeurListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurListSerializer

class ChauffeurDetailViewSet(ModelViewSet):
    queryset = Chauffeur.objects.all()
    serializer_class = ChauffeurDetailSerializer

class ClientListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer

class ClientDetailViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer

class CommandeListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Commander.objects.all()
    serializer_class = CommanderListSerializer

class CommandeDetailViewSet(ModelViewSet):
    queryset = Commander.objects.all()
    serializer_class = CommanderDetailSerializer

class VoitureListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureListSerializer

class VoitureDetailViewSet(ModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureDetailSerializer

class ConduireListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conduire.objects.all()
    serializer_class = ConduireListSerializer

class ConduireDetailViewSet(ModelViewSet):
    queryset = Conduire.objects.all()
    serializer_class = ConduireDetailSerializer
