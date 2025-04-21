import pytest
from annonces.models import User, Ville, Parcelle, Favoris, Panier, PanierItem

@pytest.mark.django_db
class TestUserModel:
    def test_user_creation(self):
        user = User.objects.create(
            email="test@example.com",
            username="testuser",
            firstname="Test",
            lastname="User",
            role="client"
        )
        assert user.email == "test@example.com"
        assert user.username == "testuser"
        assert user.role == "client"

@pytest.mark.django_db
class TestVilleModel:
    def test_ville_creation(self):
        ville = Ville.objects.create(nom="Paris")
        assert ville.nom == "Paris"

@pytest.mark.django_db
class TestParcelleModel:
    def test_parcelle_creation(self):
        user = User.objects.create(
            email="test@example.com",
            username="testuser"
        )
        ville = Ville.objects.create(nom="Paris")
        parcelle = Parcelle.objects.create(
            nom="Test Parcelle",
            prix=100000,
            user=user,
            ville=ville,
            categorie="terrain",
            description="Test description"
        )
        assert parcelle.nom == "Test Parcelle"
        assert parcelle.prix == 100000
        assert parcelle.ville == ville