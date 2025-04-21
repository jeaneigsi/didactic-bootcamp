from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    ROLES={
        ('Admin','Admin'),
        ('User','User')    
    }
    
    
    firstname=models.CharField(max_length=100,)
    lastname=models.CharField(max_length=100,)
    role=models.CharField(max_length=20,choices=ROLES, default='User')
    email=models.EmailField(max_length=100, blank=True,unique=True)
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  
        blank=True
    )

    REQUIRED_FIELDS = ['username','email','firstname','lastname']
    USERNAME_FIELD = 'email'
    
    
    
    def __str__(self):
        return f"{self.username} ({self.role})"
 
class Ville(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom
   
    
class Parcelle(models.Model):
    CATEGORIE={
        ('Residentiel','Residentiel'),
        ('Nue','Nue'),
        ('Industriel','Industriel')
    }
    nom = models.CharField(max_length=100, unique=True)
    prix=models.FloatField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ville=models.ForeignKey(Ville,on_delete=models.CASCADE)
    categorie=models.CharField(max_length=50,choices=CATEGORIE, default='Nue')
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='annonces/images', blank=True,null=True)

class Favoris(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'parcelle')  # Empêche un utilisateur de sauvegarder deux fois la même annonce

    def __str__(self):
        return f"{self.user.username} a sauvegardé {self.parcelle}"
   
   
class Panier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.user.username}"


class PanierItem(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    parcelle = models.ForeignKey(Parcelle, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('panier', 'parcelle')  # Empêche d'ajouter deux fois la même parcelle

    def __str__(self):
        return f"{self.parcelle} dans {self.panier}"
 
# Create your models here.
