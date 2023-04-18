from django.shortcuts import render
from django.core.paginator import Paginator
from compte.creation_bbd import creation_dappart, creation_des_users
from compte.tests import *
from compte.models import *
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {'navbar': 'index'})    

def go(request):
    action()
    return render(request, 'go.html')

def locataire(request):  
    locataires = Appartement.objects.all()   
    paginator = Paginator(locataires, 4)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page) 
    context = {
        "navbar" : 'locataire',
        "locataires" : pagebjets,        
    }
    return render(request,'locataire.html', context)

def profil(resquest, pk):    
    locataire = Appartement.objects.get(id=pk) 
    c = locataire.charges
    x = locataire.loyer
    y= locataire.allocation
    loyer = str((x-y)+c)    
    context={
        "loyer": loyer,
        "locataire" : locataire,
        "navbar" : 'locataire',
        }
    return render(resquest, 'profils.html', context)

def annonce(request):
    context={
        "navbar" : 'Annonce',
    }
    return render(request, 'annonce.html',context)


