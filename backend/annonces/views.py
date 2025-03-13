# viewset est ma classe specilaisé qui va permettre les opérations CRUD avec ma base de données
from rest_framework import viewsets

from .models import User,Ville,Parcelle,Favoris,Panier,PanierItem
from .serializers import UserSerializers,VilleSerializer,ParcelleSerializer,FavorisSerializer,PanierSerializer,PanierItemSerializer
from django.http import JsonResponse


# Create your viewsets here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all() # recupere tout user de ma BDD
    serializer_class=UserSerializers # lie le vieset à un Serializer
    
class VilleViewSet(viewsets.ModelViewSet):
    queryset=Ville.objects.all()
    serializer_class=VilleSerializer
    
class ParcelleViewSet(viewsets.ModelViewSet):
    queryset=Parcelle.objects.all()
    serializer_class=ParcelleSerializer
    
class FavorisViewSet(viewsets.ModelViewSet):
    queryset=Favoris.objects.all()
    serializer_class=FavorisSerializer
    
    
class PanierViewSet(viewsets.ModelViewSet):
    queryset = Panier.objects.all()
    serializer_class = PanierSerializer
    
class PanierItemViewSet(viewsets.ModelViewSet):
    queryset = PanierItem.objects.all()
    serializer_class = PanierItemSerializer