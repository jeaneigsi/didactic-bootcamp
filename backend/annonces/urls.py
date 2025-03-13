from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,VilleViewSet,ParcelleViewSet,FavorisViewSet,PanierViewSet,PanierItemViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .auth_views import CustomAuthToken
from django.http import HttpResponse



# créons les routes 

router=DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'villes', VilleViewSet)
router.register(r'parcelles', ParcelleViewSet)
router.register(r'favoris', FavorisViewSet)
router.register(r'paniers', PanierViewSet)
router.register(r'panieritems', PanierItemViewSet)



# Liste les URLs enregistrées dans le routeur
urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    
]
