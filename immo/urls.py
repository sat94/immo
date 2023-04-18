from django.contrib import admin
from rest_framework import routers
from immo import settings
from django.conf.urls.static import static
from administration.views import *
from .views import *
from compte.views import *
from django.urls import path, include
from compte.urls import router as todo_router
from Quitance.views import *

router = routers.DefaultRouter()
router.registry.extend(todo_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', IndexView.as_view(), name='index'), 
    path('go/', go, name='go'),
    path('api/',include(router.urls)),
    path('locataire/',locataire,name='locataire'), 
    path('login/',include ('django.contrib.auth.urls')),
    path('appartement/',appartement, name='appartement'),
    path('appartement/<int:pk>', profil,name='appart'),
    path('paiement/', paiement, name='paiement'),  
    path('administration/', administration, name='administration'), 
    path('ajouter/appartement', ajouter_appartement, name='ajouter_appartement'),  
    path('ajouter/locataire', ajouter_locataire, name='ajouter_locataire'),  
    path('cherche/', cherche_locataire, name='cherche_locataire'),
    path('cherche/appartement', cherche_appartement, name='cherche_appartement'), 
    path('cherche/paie', cherche_paie, name='cherche_paie'),     
    path('modif/appartement/<int:pk>', modifier_appartement,name='modif_appartement'),
    path('modif/locataire/<int:pk>', modifier_Locataire,name='modif_locataire'),
    path('valide/appartement/<int:pk>', valide_appartement,name='valide'),
    path('valide/locataire/<int:pk>', valide_locataire,name='loc_valide'),    
    path('delete/appartement/<int:pk>', delete_appartement,name='delete_appartement'),    
    path('delete/locataire/<int:pk>', delete_locataire,name='delete_locataire'),  
    path('quitance/<int:pk>', quitance, name='quitance'),
    path('mail/<int:pk>',send_email,name='send_email'),
    path('paiement/graphique', graphique ,name='graphique')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

