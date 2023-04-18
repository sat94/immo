import locale
from django.shortcuts import render
from compte.views import Appartement, Locataire
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
import pandas as pd 
from plotly.offline import plot
import plotly.express as px
import datetime
from django.db.models import Sum

import datetime

def quitance(request, pk):
    locataire = Appartement.objects.get(id=pk)
    c = locataire.charges
    x = locataire.loyer
    y= locataire.allocation
    loyer = str((x-y)+c)
    date = datetime.datetime.today()
    context = {
        'date' : date,
        'locataire' : locataire,
        'Total' : loyer
    }
    return render(request, "quitance.html", context)

def send_email(request, pk):
    locataire = Appartement.objects.get(id=pk)
    email = locataire.user.email
    html_content= render_to_string('email.html', {'locataire': locataire})  
    text_content = strip_tags(html_content)
    send_mail(
    'Votre quitance de loyer',
    text_content,
    'amonuta39@gmail.com',
    [email],
    html_message=html_content,
    fail_silently=False,)
    context = {
        'locataire' : locataire
    }
    return render(request, "quitance.html", context)

def graphique(request):
    locataire = Appartement.objects.all()
    Nbappart = Appartement.objects.all().count
    Nbloca = Locataire.objects.all().count
    qs = locataire
    project = [
        {
            'Nom': x.user.nom,
            'Loyer': x.loyer,           
            'Prenom' : x.user.prenom
        } for x in qs
    ]
    df = pd.DataFrame(project)    
    fig = px.bar(df, x ="Nom", y="Loyer" , color="Prenom")
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.layout.legend = {'font_color':'white'}
    fig.update_xaxes({'color':'white'})
    fig.update_yaxes({'color':'white'})  
    gantt_plot = plot(fig, output_type="div")
    end_date = datetime.datetime.today()
    date = [
        {
            'Nom' : x.user.nom,
            'Start': x.date,
            'Finish': end_date,
            'Prenom' : x.user.prenom
        } for x in qs
    ] 
    df = pd.DataFrame(date)   
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Nom", color="Prenom")
    fig.layout.plot_bgcolor = 'black'
    fig.layout.paper_bgcolor = 'black'
    fig.layout.legend = {'font_color':'white'}
    fig.update_xaxes({'color':'white'})
    fig.update_yaxes({'color':'white'}) 
    fig.update_yaxes(autorange='reversed')
    gantt = plot(fig, output_type="div")
    
    agence = Appartement.objects.filter(agence=True).count()
    retard = Appartement.objects.filter(solde=False).count()  

    total = Appartement.objects.aggregate(Sum('loyer'))['loyer__sum']
    com = agence * 0.8
    var = total - com
    commision = total - var

    locale.setlocale(locale.LC_ALL, '')  # Utilise la configuration régionale du système

    nombre = total
    nombre_formate = locale.format_string("%d", nombre, grouping=True)




    context = {
        'Nbappart' : Nbappart,
        'Nbloca': Nbloca,
        'locataire' : locataire,
        "graph" : gantt_plot, 
        "graph1" : gantt, 
        'agence' : agence,  
        'retard' : retard,
        'total'  : nombre_formate,
        'commi' : commision
    }
    return render(request,'graphique.html', context)

    
    