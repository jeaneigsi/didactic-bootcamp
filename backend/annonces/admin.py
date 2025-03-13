from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User, Ville, Parcelle, Favoris, Panier, PanierItem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
admin.site.site_header = "Gestion des Annonces - Admin"
admin.site.site_title = "Administration Annonces"
admin.site.index_title = "Bienvenue sur l'espace d'administration"

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display=('id', 'username', 'firstname', 'lastname', 'email', 'role', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields=( 'username', 'firstname', 'lastname', 'email')
    ordering = ('id',)
    fieldsets = (
        ("Informations personnelles", {"fields": ("username", "email", "firstname", "lastname", "role")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )



# Personnalisation de la VilleAdmin
@admin.register(Ville)
class VilleAdmin(ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)

# Personnalisation de la ParcelleAdmin
@admin.register(Parcelle)
class ParcelleAdmin(ModelAdmin):
    list_display = ('id', 'nom', 'prix', 'categorie', 'ville', 'created_at')
    list_filter = ('categorie', 'ville')
    search_fields = ('nom', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        ("Détails de la Parcelle", {"fields": ("nom", "prix", "categorie", "description", "ville", "user", "image")}),
        ("Dates", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ('created_at', 'updated_at')  # Pour éviter de modifier ces champs

# Personnalisation des Favoris
@admin.register(Favoris)
class FavorisAdmin(ModelAdmin):
    list_display = ('id', 'user', 'parcelle', 'created_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'parcelle__nom')

# Personnalisation du Panier
@admin.register(Panier)
class PanierAdmin(ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__username',)

# Personnalisation des PanierItems
@admin.register(PanierItem)
class PanierItemAdmin(ModelAdmin):
    list_display = ('id', 'panier', 'parcelle', 'added_at')
    search_fields = ('parcelle__nom',)