from rest_framework import serializers
from compte.models import *


class AdresseSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields ='__all__'

class MyUserSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields ='__all__'

class AppartementSeiralizer(serializers.ModelSerializer):
    adresse = AdresseSeiralizer(read_only=True)
    city = AdresseSeiralizer(many=True, read_only=True)
    class Meta:
        model = Appartement
        fields ='__all__'
    
class LocataireSeiralizer(serializers.ModelSerializer):
    locataire = AppartementSeiralizer(many=True, read_only=True)
    class Meta:
        model = Locataire
        fields ='__all__'            
        

        
    

    