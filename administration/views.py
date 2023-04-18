from django.shortcuts import render, redirect
from compte.views import Appartement
from django.core.paginator import Paginator
from administration.forms import *
from django.contrib import messages
from django.db.models import Q
import datetime
import os


def delete_previous_picture(previous,new):
    if previous != new:
        os.remove(previous)
        return True
    return False    

def delete_previous_pictures(previous):
    os.remove(previous)
    return True
   
def administration(request):
    locataires = Appartement.objects.all()   
    paginator = Paginator(locataires, 7)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page) 
    context={
        "navbar" : 'administration',
        "locataires" : pagebjets,
    }
    return render(request, 'admisnistration.html', context)

def appartement(request):
    locataires = Appartement.objects.all()   
    paginator = Paginator(locataires, 9)
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page)
    context={
        'navbar' : 'appartement',
        "locataires" : pagebjets,
    }
    return render(request, "appartement.html", context)

def paiement(request):
    locataires = Appartement.objects.all()     
    paginator = Paginator(locataires, 13) 
    page = request.GET.get('page')
    pagebjets = paginator.get_page(page) 
    context={        
        "navbar" : "paiement",
        "locataires" : pagebjets,      
    }
    return render(request, 'paiement.html', context)

def ajouter_appartement(request): 
    init_values = {}
    init_values["date"]= datetime.datetime.today()
    forms = Appartementform(initial=init_values)     
    if request.method == "POST":
        forms = Appartementform(request.POST)  
        if forms.is_valid():
            forms.save()
            messages.success(request,"l'appartement a été Ajouter!")
            return redirect('index')
        else:
            print(forms.errors)
            forms = Appartementform()         
            messages.error(request, f'Nous avons pas pu envoyer votre formulaire car il comporte des erreurs')
    context={
        'form' : forms,
        "navbar" : "ajouter"
    }
    return render(request, 'ajouter_appartement.html', context)

def ajouter_locataire(request): 
    forms = LocataireForm()
    if request.method == "POST":
        print(request.POST)
        forms = LocataireForm(request.POST, request.FILES)  
        if forms.is_valid():
            forms.save()
            messages.success(request,"le locataire a été Ajouter!")
            return redirect('ajouter_appartement')
        else:
            print(forms.errors)
            messages.error(request, f'Nous avons pas pu envoyer votre formulaire car il comporte des erreurs')
            forms = LocataireForm()          
    context={
        'form' : forms,
        "navbar" : "ajouter"
    }
    return render(request, 'ajouter_locataire.html', context)

def cherche_locataire(request):
    cherche = request.POST.get('cherche')
    loca = Appartement.objects.filter(Q(user__prenom__icontains=cherche)  |
                                      Q(user__nom__icontains=cherche) |
                                      Q(user__email__icontains=cherche) |
                                      Q(adresse__nom_commune__icontains=cherche) |
                                      Q(adresse__nom_voie__icontains=cherche) |
                                      Q(adresse__code_postal__icontains=cherche))                                   
    context = {"locataires" : loca}
    return render(request,'admisnistration.html', context)

def cherche_appartement(request):
    cherche = request.POST.get('cherche')
    loca = Appartement.objects.filter(Q(user__prenom__icontains=cherche)  |
                                    Q(user__nom__icontains=cherche) |
                                    Q(user__email__icontains=cherche) |
                                    Q(adresse__nom_commune__icontains=cherche) |
                                    Q(adresse__nom_voie__icontains=cherche) |
                                    Q(observation__icontains=cherche) |
                                    Q(etat__icontains=cherche) |
                                    Q(sanitaire__icontains=cherche) |
                                    Q(piece__icontains=cherche) |
                                    Q(date__icontains=cherche))                                   
    context = {"locataires" : loca}
    return render(request, "appartement.html", context)

def cherche_paie(request):
    cherche = request.POST.get('cherche')
    loca = Appartement.objects.filter(Q(user__prenom__icontains=cherche)  |
                                    Q(user__nom__icontains=cherche) |
                                    Q(user__email__icontains=cherche) |
                                    Q(adresse__nom_commune__icontains=cherche) |
                                    Q(adresse__nom_voie__icontains=cherche) |
                                    Q(caution__icontains=cherche)|
                                    Q(loyer__icontains=cherche) |
                                    Q(solde__icontains=cherche))                                   
    context = {"locataires" : loca}
    return render(request, 'paiement.html', context)

def modifier_appartement(request, pk):
    appartement = Appartement.objects.get(id=pk)    
    forms = Appartform(instance=appartement)          
    context={
        'appartement' : appartement,
        'form' : forms,
        "navbar" : "appartement"
    }
    return render(request, 'modif_appart.html', context)

def modifier_Locataire(request, pk):
    appartement = Locataire.objects.get(id=pk)    
    forms = LocataireForm(instance=appartement)          
    context={
        'appartement' : appartement,
        'form' : forms,
        "navbar" : "appartement"
    }
    return render(request, 'modif_locataire.html', context)

def valide_locataire(request, pk):
    part = Locataire.objects.get(id=pk) 
    if part.photo:
        default_image_path = part.photo.path      
    form = LocataireForm(request.POST or None, request.FILES or None, instance=part) 
    if request.method == 'POST':       
        if form.is_valid():
            if len(request.FILES)!= 0:
                delete_previous_picture(default_image_path, part.photo.path)       
            form.save() 
            messages.success(request,"l'appartement a été modifier!")
            return redirect('index')
    else:
        redirect('appartement')  

def valide_appartement(request, pk):
    part = Appartement.objects.get(id=pk)        
    form = Appartform(request.POST or None, instance=part) 
    if request.method == 'POST':       
        if form.is_valid():           
            form.save() 
            messages.success(request,"l'appartement a été modifier!")
            return redirect('index')
    else:
        redirect('appartement')    
   
def delete_appartement(request, pk):   
    app= Appartement.objects.filter(id=pk) 
    app.delete()
    messages.success(request,"l'appartement a été supprimer!") 
    return redirect('index')

def delete_locataire(request, pk):   
    part = Locataire.objects.get(id=pk)
    default_image_path = part.photo.path
    part.delete()
    delete_previous_pictures(default_image_path) 
    messages.success(request,"le locataire a été supprimer!") 
    return redirect('index')