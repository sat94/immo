from django import forms
from compte.models import Appartement, Locataire

class Appartementform(forms.ModelForm):    
    def __init__(self, *args, **kwargs):
        super(Appartementform, self).__init__(*args, **kwargs)
        CUSTOM_QUERYSET = Locataire.objects.filter(locataire__isnull=True)        
        self.fields['user'].queryset = CUSTOM_QUERYSET
    class Meta:
        model = Appartement     
        fields = [
            "user",
            "piece",
            "loyer", 
            "charges",
            "caution" ,
            "sanitaire" , 
            "agence" ,
            "numeros" ,    
            "etat" ,
            "observation" , 
            "adresse" ,
            "date"
            ]
        labels = {
            "user" : "Locataire",
            "piece" : "Nombre de piece",
            "sanitaire" : "Sanitaire" ,
            "caution" : "Montant de la caution",
            "charges": "Montant des charges",
            "loyer" : "Montant du loyer",
            "agence" : "Apartiens à L'agence",
            "etat" : "Etat",
            "observation" : "Observation",
            "numeros" : "Numeros de la rue" ,  
            "adresse" : "Adresse",                        
        }
        widgets = {       
         
            "observation" : forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ),                    
        }        
        def clean_appart(self):
            observation = self.cleaned_data.get("observation")  
            if "$" in observation:
                raise forms.ValidationError("Le pseudo ne peut pas contenir de dollar")
            return observation

class Appartform(forms.ModelForm):  
    class Meta:
        model = Appartement     
        fields = '__all__'
        labels = {
            "user" : "Locataire",
            "piece" : "Nombre de piece",
            "sanitaire" : "Sanitaire" ,
            "caution" : "Montant de la caution",
            "charges": "Montant des charges",
            "loyer" : "Montant du loyer",
            "agence" : "Apartiens à L'agence",
            "etat" : "Etat",
            "observation" : "Observation",
            "numeros" : "Numeros de la rue" ,  
            "adresse" : "Adresse",                        
        }
        widgets = {       
         
            "observation" : forms.Textarea(
                 attrs={
                    'rows': 5,
                    'cols': 50,
                }
                ),                    
        }        
        def clean_appart(self):
            observation = self.cleaned_data.get("observation")  
            if "$" in observation:
                raise forms.ValidationError("Le pseudo ne peut pas contenir de dollar")
            return observation
        
        
class LocataireForm(forms.ModelForm):
    class Meta:
        model = Locataire      
        exclude = ['Nbcontrat']
        
    def clean_locataire(self):
        nom = self.cleaned_data.get("nom")   
              
        if "$" in nom:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de dollar")
        return nom
    

    