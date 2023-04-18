import json
import random



prenoms_malle = ["Axel","Adrien","Augustin","Amaury","Bastien","Arthur","Alban","Alexis","Antoine","Auguste","Benjamin",
           "Achille","Adam","Alexandre","Baptiste","Aaron","Antonin","Armand","Basile","Elias","Diego","Esteban","Dylan","David",
           "Emile","Daniel","Erwan","Charles","Clement","Corentin","Enzo","Jean","Felix","Evan","Gabriel","Marc","Julien",
           "Idriss","Isaac","Joseph","Jules","Jean","Hugo","Léo","Lucien","Mathias","Marin","Marius","Lorenzo","Mael","Maxime","Lois",
           "Louis","Mateo","Leonard","Luca","Marcel","Mathis","Léon","Lucas","Matteo","Martin","Pierre","Quentin",
           "Nicolas","Raphaël","Oscar","Paul","Noé","Pablo","Rafael","Nathan","Romain","Theo","Samuel","Simon",
           "Robin","Romeo","Victor","Youssef","Tiago","Tom","Tristan","William","Abel","Thibault","Thomas","Valentin","Adem","Ali",
           "Ahmed","Alessio","Amir","Bilal","Charly","Elio","Ethan","Eliot","Eliott","Sebastien","Serge","Steve",
           "Richard","Antoine","Thomas","Auguste","Steve","Addam","Kevin","Frédéric"]

prenoms_feminin = ["Sabrina","Sylvie","Delphine","Sabine","Jennifer","Stephanie","Sophie","Mélani","Sophia","Marguerite","Patricia","Marilyn",
                   "Frédérique","Magali","Nathalie","Béatrice","Aline","Sarah","Matilde","Laurence","Christine","Cindy","Anne","Stacy","Angela",
                   "Aurélie","Fatima","Salma","Nadia","Catherine","Eveline","Hélène","Alexia","Véronique","Marie","Jessica","Emma","Emmanuelle",
                   "Laura","Clara","Sandrine","Chloé","Joséphine","Anissa","Anaisse","Eveline","Michelle","Marinne","Louise","Félicité","Virgini",
                   "Cyntia","Jade","Emma","Ambre","Alice","Lina","Rose","Mia","Léa","Julia","Julie","Léna","zoé","Nina","Eva","Charlie","Lola",
                   "Victoire","Manon","Luna","Camille","Lucie","Olivia","Alix","Sofia","Charlotte","Margot","Lyana","Capucine","Clémence",
                    "Théa","Hélena","Alba","Emy","Aya","Yasmine","Roxane","Zélie","Mathilde","Valentine","Anaïs","Lila","Joy","Maëlle",
                  "Amélia","Elsa","Noémie","Salomé","Nora","Soline" ]
                   
noms_de_famille = ["Martas","Bernard","Thomasia","Petit","Roberty","Richard","Durand","Dubois","Moreau","Laurentino",
           "Simon","Michel","Lefebvre","Leroy","Roux","Davra","Bertrand","Morel","Fournier","Girard","Bonnet",
           "Dupont","Lambert","Fontaine","Rousseau","Vincy","Muller","Lefevre","Faure","Andrea","Mercier","Blanc",
           "Guerin","Boyer","Garnier","Chevalier","France","Legrand","Gauthier","Garcia","Perrin","Robin","Clemare",
           "Morin","Henry","Roussel","Math","Gautier","Masson","Marchand","Duval","Denis","Dumont","Maritina","Lemaire",
           "Noel","Meyer","Dufour","Meunier","Brun","Blanchard","Giraud","Joly","Riviere","Lucas","Brunet","Gaillard",
           "Barbier","Arnauder","Martinez","Gerarda","Roches","Renard","Schmitt","Roy","Leroux","Colin","Vidal","Caron",
           "Picard","Rogerera","Fabre","Aubert","Lemoine","Renaud","Dumas","Lacroix","Oliviera","Philippe","Bourgeois",
           "Pierre","Benoit","Rey","Leclerc","Payet","Rolland","Leclercq","Guillaume","Lecomte","Lopez","Jean","Dupuy",
           "Guillot","Hubert","Berger","Carpentier","Sanchez","Dupuis","Moulin","Louis","Deschamps","Huet","Vasseur",
           "Perez","Boucher","Fleury","Royer","Klein","Jacquet","Adam","Paris","Poirier","Marty","Aubry","Guyot","Carre",
           "Charles","Renault","Charpentier","Menard","Maillard","Baron","Bertin","Bailly","Herve","Schneider","Fernandez",
           "Le Gall","Collet","Leger","Bouvier","Julien","Prevost","Millet","Perrot","Daniel","Le Roux","Cousin","Germain",
           "Breton","Besson","Langlois","Remy","Le Goff","Pelletier","Leveque","Perrier","Leblanc","Barre","Lebrun","Marchal",
           "Weber","Mallet","Hamon","Boulanger","Jacob","Monnier","Michaud","Rodriguez","Guichard","Gillet","Etienne","Grondin",
           "Poulain","Tessier","Chevallier","Collin","Chauvin","Da Silva","Bouchet","Lemaitre","Benard","Marechal","Humbert",
           "Reynaud","Hoarau","Perret","Barthelemy","Cordier","Pichon","Lejeune","Gilbert","Lamy","Delaunay",
           "Pasquier","Carlier","Laporte","Gautier","Ncoucou","Deville","Chateau","Fleuve"]


def creation_des_users():
    locas= []
    x=1
    y=1
    i=1   
    for i in range(200):   
        sexe = random.randint(1,2)
        nom = random.choice(noms_de_famille)
        if sexe == 1:
            loca = {
                "nom": nom,
                "email": nom + str(i) + random.choice(["1@live.fr","1@gmail.fr","1@yahoo.fr","1@hotmail.com","1@wanadoo.fr"]),
                "prenom": random.choice(prenoms_malle),
                "photo": "photo/homme_"+str(y)+".jpeg",           
                "numberPhone": "0" + random.choice(["1",str(random.randint(6,7)),"9"])+ str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)),               
                "sexe" : "homme",
                "Solde": random.choice(bool(random.getrandbits(1)),True,True),   
            }
            y=y+1
        else:
            loca = {                
                "nom": str(nom),
                "email": nom + str(i) + random.choice(["1@live.fr","1@gmail.fr","1@yahoo.fr","1@hotmail.com","1@wanadoo.fr"]),
                "prenom": random.choice(prenoms_feminin),
                "photo": "photo/femme_"+str(x)+".jpeg",              
                "numberPhone": "0" + random.choice(["1",str(random.randint(6,7)),"9"])+ str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)) + str(random.randint(10, 99)),            
                "sexe" : "femme",
                "Solde": random.choice(bool(random.getrandbits(1)),True,True),    
            }
            x=x+1
        print(loca)
        locas.append(loca)
        i=i+1
                
    json_data = {
        "locataire": locas,        
    }
    with open('locataire.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False, sort_keys=True)

sanitaire=['cuisine, salle de bain, (wc) à part','cuisine américaine, salle de bain, (wc) à part','cuisine, salle de bain(wc)','cuisine américaine, salle de bain, (wc) à part','cuisine, salle de bain (wc)']
piece =['1 piece','2 piece','3 piece','4 piece','5 piece','6 piece']
        
def creation_dappart():
    jour = random.randint(1,25)
    moi = random.randint(1,12)
    annee = "20"+ str(random.randint(10,22)) 
    apparts = []
    for i in range(200):
        solde = True
        montant = 0
        x = random.randint(1,100)
        if x<90 :      
            r = "bon"
            y = "Rien a signaler" 
        elif x>90 and x<98:
            solde = False
            montant = random.randint(1,3)        
        else:
            x = random.randint(1,3)
            match x:
                case "1":
                    r =  "bon"
                    y = "Fuite d'eau"
                
                case "2":
                    r =  "correct"
                    y = "Trou sur des murs"
                
                case "3":
                    r =  "problem"
                    y = "Le chaufage ne marche plus"     
        it = random.choice(piece)      
        match it: 
            case '1 piece':
                appart = {
                    "loyer": "400",
                    "caution":  "800",
                    "sanitaire" :  random.choice(sanitaire),
                    "agence": bool(random.getrandbits(1)),
                    "numéros": random.randint(1,200),
                    "piece"  : it,
                    "solde" : solde,
                    "montant" : montant,
                    "etat" : r,
                    "observation" : y,                  
                    "allocation": random.randint(0,100),
                    }
            case '2 piece':
                appart = {
                    "loyer": "600",
                    "caution":  "1200",
                    "sanitaire" :  random.choice(sanitaire),
                    "agence": bool(random.getrandbits(1)),
                    "numéros": random.randint(1,200), 
                    "piece"  : it ,
                    "solde" : solde,
                    "montant" : montant,
                    "etat" : r,
                    "observation" : y,                   
                    "allocation": random.randint(0,200),
                    }
            case '3 piece':
                appart = {
                    "loyer": "1000",
                    "caution":  "2000",
                    "sanitaire" :  random.choice(sanitaire),
                    "agence": bool(random.getrandbits(1)),
                    "numéros": random.randint(1,200),
                    "solde" : solde,
                    "montant" : montant,  
                    "piece"  : it,
                    "etat" : r,
                    "observation" : y,                  
                    "allocation": random.randint(0,600),
                    }
            case '4 piece':
                appart = {
                    "loyer": "1200",
                    "caution":  "2400",
                    "sanitaire" :  random.choice(sanitaire),
                    "agence": bool(random.getrandbits(1)),
                    "numéros": random.randint(1,200),
                    "solde" : solde,
                    "montant" : montant,
                    "piece"  : it ,
                    "etat" : r,
                    "observation" : y,                  
                    "allocation": random.randint(0,800),
                    }
            case '5 piece':
                appart = {
                    "loyer": "1500",
                    "caution":  "3000",
                    "sanitaire" :  random.choice(sanitaire),
                    "agence": bool(random.getrandbits(1)),
                    "numéros": random.randint(1,200),
                    "solde" : solde,
                    "montant" : montant, 
                    "piece"  : it,
                    "etat" : r,
                    "observation" : y,                  
                    "allocation": random.randint(0,1000),
                    }
            case '6 piece':
                appart = {
                    "loyer": "1900",
                    "caution":  "3800",
                    "sanitaire" :  random.choice(sanitaire),
                    "agence": bool(random.getrandbits(1)),
                    "numéros": random.randint(1,200),
                    "solde" : solde,
                    "montant" : montant,
                    "piece"  : it ,
                    "etat" : r,
                    "observation" : y,                  
                    "allocation": random.randint(0,1400),
                    } 
        apparts.append(appart)
        print(appart)
        i=i+1
                
    
    json_data = {
        "appartement": apparts,             
    }
    with open('appartements.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False, sort_keys=True)
