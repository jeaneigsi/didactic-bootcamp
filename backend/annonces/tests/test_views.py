import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from annonces.models import User, Ville, Parcelle

@pytest.mark.django_db
class TestParcelleAPI:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@example.com",
            username="testuser"
        )
        self.ville = Ville.objects.create(nom="Paris")
        self.parcelle = Parcelle.objects.create(
            nom="Test Parcelle",
            prix=100000,
            user=self.user,
            ville=self.ville,
            categorie="terrain",
            description="Test description"
        )
        
    def test_list_parcelles(self):
        url = reverse('parcelle-list')  # Assurez-vous que ce nom correspond à votre URL
        response = self.client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 1  # Vérifie qu'il y a une parcelle dans la réponse