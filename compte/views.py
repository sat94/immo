from django.shortcuts import render, redirect
from django.contrib.auth import logout
from compte.models import *
from rest_framework import viewsets
from compte.serializers import *



def login(request):
    return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('index')



class MyUserView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSeiralizer


class LocataireView(viewsets.ModelViewSet):
    queryset = Locataire.objects.all()
    serializer_class = LocataireSeiralizer
    def create(self, request, *args, **kwargs):
        # Logique de création d'un nouveau locataire
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # Logique de récupération d'un locataire par son identifiant
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Logique de mise à jour d'un locataire existant
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # Logique de mise à jour partielle d'un locataire existant
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Logique de suppression d'un locataire existant
        return super().destroy(request, *args, **kwargs)
    
class AppartementView(viewsets.ModelViewSet):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSeiralizer
    def create(self, request, *args, **kwargs):
        # Logique de création d'un nouveau locataire
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # Logique de récupération d'un locataire par son identifiant
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Logique de mise à jour d'un locataire existant
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # Logique de mise à jour partielle d'un locataire existant
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Logique de suppression d'un locataire existant
        return super().destroy(request, *args, **kwargs)
    

class AdresseView(viewsets.ModelViewSet):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSeiralizer
    def create(self, request, *args, **kwargs):
        # Logique de création d'un nouveau locataire
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        # Logique de récupération d'un locataire par son identifiant
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Logique de mise à jour d'un locataire existant
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        # Logique de mise à jour partielle d'un locataire existant
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Logique de suppression d'un locataire existant
        return super().destroy(request, *args, **kwargs)
    
    
