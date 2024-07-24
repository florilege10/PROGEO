from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    ChauffeurListViewSet, ChauffeurDetailViewSet,
    ClientListViewSet, ClientDetailViewSet,
    CommandeListViewSet, CommandeDetailViewSet,
    VoitureListViewSet, VoitureDetailViewSet,
    ConduireListViewSet, ConduireDetailViewSet
)

router = SimpleRouter()
router.register(r'chauffeurs', ChauffeurListViewSet, basename='chauffeur-list')
router.register(r'chauffeur', ChauffeurDetailViewSet, basename='chauffeur-detail')
router.register(r'clients', ClientListViewSet, basename='client-list')
router.register(r'client', ClientDetailViewSet, basename='client-detail')
router.register(r'commandes', CommandeListViewSet, basename='commande-list')
router.register(r'commande', CommandeDetailViewSet, basename='commande-detail')
router.register(r'voitures', VoitureListViewSet, basename='voiture-list')
router.register(r'voiture', VoitureDetailViewSet, basename='voiture-detail')
router.register(r'conduires', ConduireListViewSet, basename='conduire-list')
router.register(r'conduire', ConduireDetailViewSet, basename='conduire-detail')

urlpatterns = [
    path('', include(router.urls)),
]
