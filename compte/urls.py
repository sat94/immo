from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register('user', MyUserView)
router.register('locataire', LocataireView)
router.register('appartement', AppartementView)
router.register('adresse', AdresseView)
