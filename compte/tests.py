from compte.models import *
from pathlib import Path
import random
import json

                
def insert_users():
    file = Path.cwd() / "compte/locataire.json" 
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    for row in datas:       
        loca = Locataire(id=None,nom=row['nom'],prenom=row['prenom'], numberPhone=row['numberPhone'],                         
                          email =row["email"],sexe=row['sexe'],
                         photo=row['photo'])
        print(loca)
        loca.save()


                
def insert_appart(): 
    pegase = [] 
    def hasard():
        num = random.randint(1,6535)
        return num if num not in pegase else hasard()
    file = Path.cwd() / "compte/appartements.json" 
    with open(file, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    i=1        
    for row in datas["appartement"]:        
        z = hasard()       
        while z in pegase:
            hasard()
            pegase.append(z) 
        if z in pegase:
            hasard() 
        else:
            pegase.append(z)
            
        jour = random.randint(1,25)
        moi = random.randint(1,12)
        annee = "20"+ str(random.randint(10,22))  
        users = Locataire.objects.get(id=i)
        licorne = Adresse.objects.get(id=z) 
        appart = Appartement(id=None,user=users,piece = row["piece"],loyer = row["loyer"],caution = row['caution'], sanitaire = row['sanitaire'],allocation = row["allocation"],date = str(annee) + "-" + str (moi) + "-" + str(jour),
                           agence = bool(random.getrandbits(1)),numeros = row['numéros'],etat=row['etat'],observation=row['observation'],charges=str(random.randint(30,90)),adresse=licorne,solde=row['solde'],montant=row['montant'])   
        i=i+1
        appart.save()         

def insert_lieux():  
    with open(r"C:\Users\Shadow\Desktop\immo\src\compte\data.csv", "r",encoding="utf8") as f:
        datas = f.readlines() 
        data = 2 
        for data in datas:           
            try:                
                lieu = Adresse(id=None,nom_commune = data.split(';')[2],  nom_voie = data.split(';')[0],code_postal = data.split(';')[1],x =data.split(';')[3],y =data.split(';')[4] ,geo =data.split(';')[5])           
                lieu.save()
            except:
              print(str(lieu))     
 
  
def action(): 
    insert_lieux()  
    insert_users()
    insert_appart()
   
    