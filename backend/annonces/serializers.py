from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User,Ville,Parcelle,Favoris,Panier,PanierItem

User=get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','firstname','lastname','role']
        
class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ville
        fields='__all__'
        
class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parcelle
        fields='__all__'
        
class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favoris
        fields='__all__'
        
class PanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'
        
class PanierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanierItem
        fields = '__all__'
