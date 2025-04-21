# Dans un fichier conftest.py dans le répertoire tests
import pytest
from annonces.models import User, Ville, Parcelle

@pytest.fixture
def user():
    return User.objects.create(
        email="test@example.com",
        username="testuser",
        firstname="Test",
        lastname="User",
        role="client"
    )

@pytest.fixture
def ville():
    return Ville.objects.create(nom="Paris")

@pytest.fixture
def parcelle(user, ville):
    return Parcelle.objects.create(
        nom="Test Parcelle",
        prix=100000,
        user=user,
        ville=ville,
        categorie="terrain",
        description="Test description"
    )