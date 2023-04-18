from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django_resized import ResizedImageField

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur")         
        username = self.model.normalize_username(username)            
        user = self.model(username=username, password=password)
        user.set_password(password)
        user.save()
        return user
            
    def create_superuser(self, username, password=None):
        username = self.model.normalize_username(username)           
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
    
permi = [
    ('Commercial', 'Commercial'),
    ('Administrateur', 'Administrateur'),
]
    
class MyUser(AbstractBaseUser): 
    username = models.CharField(unique=True, max_length=30, blank=False)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    permission = models.CharField(choices= permi, max_length=15, default="commercial", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
    USERNAME_FIELD = "username"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True 
    
piece ={
    ('1 piece','1 piece'),
    ('2 piece','2 piece'),
    ('3 piece','3 piece'),
    ('4 piece','4 piece'),
    ('5 piece','5 piece'),
    ('6 piece','6 piece'),
}

sanitaire={
    ('Cuisine, salle de bain, (wc) à part','Cuisine, salle de bain, (wc) à part'),
    ('Cuisine américaine, salle de bain, (wc) à part','Cuisine américaine, salle de bain, (wc) à part'),
    ('Cuisine, salle de bain(wc)','Cuisine, salle de bain(wc)'),
    ('Cuisine américaine, salle de bain (wc)','Cuisine américaine, salle de bain (wc)'),    
}

sexe = [
    ('homme', 'homme'),
    ('femme', 'femme'),
]

etat = [
    ('bon', 'Bon'),
    ('correct', 'Correct'),
    ('Abimé', 'Abimé'),
    ('Insalubre','Insalubre'),
]

class Locataire(models.Model):   
    email = models.EmailField(unique=True, max_length=30, blank=False) 
    Nbcontrat = models.CharField(max_length=20)   
    nom = models.CharField(max_length=20)      
    prenom = models.CharField(max_length=20)
    photo = ResizedImageField(size=[250, 350], quality=85, upload_to='photo', default=None)       
    sexe = models.CharField(choices=sexe,max_length=20)
    phone = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    numberPhone = models.CharField(validators = [phone], max_length = 10) 
        
    def __str__(self):       
        return str(self.nom + " "+ self.prenom)         
 
    def save(self, *args, **kwargs):
        self.Nbcontrat = id(Locataire)               
        super().save(*args, **kwargs)     
   
class Appartement(models.Model):
    user = models.ForeignKey(Locataire, on_delete=models.SET_NULL, null=True, blank=True, related_name='locataire')
    piece = models.CharField(choices=piece, max_length=100)
    loyer = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) 
    charges = models.IntegerField()
    allocation = models.IntegerField(null=True, blank=True)
    caution = models.IntegerField()
    sanitaire = models.CharField(choices=sanitaire, max_length=100)
    solde = models.BooleanField(default=False) 
    montant = models.IntegerField() 
    agence = models.BooleanField(default=True) 
    etat = models.CharField(choices=etat, max_length=20)
    observation = models.CharField(max_length=200) 
    numeros = models.IntegerField()    
    adresse = models.OneToOneField('compte.Adresse', on_delete=models.SET_NULL, null=True, blank=True)
     
    def save(self, *args, **kwargs):
        self.montant = 0
        self.solde = True             
        super().save(*args, **kwargs)    
    
    class Meta:
        ordering = ['id'] 
    
    def __str__(self):       
        return str(self.user)

class Adresse(models.Model):   
    nom_commune = models.CharField(max_length=50)
    nom_voie = models.CharField(max_length=50, unique=True)
    code_postal = models.CharField(max_length=10)
    x = models.CharField(max_length=10)
    y = models.CharField(max_length=10)
    geo= models.CharField(max_length=10)    
           
    def __str__(self):
          return self.nom_voie+ ", " + self.nom_commune
    
    