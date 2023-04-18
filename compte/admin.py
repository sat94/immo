from django.contrib import admin
from compte.models import *

admin.site.register(MyUser)




@admin.register(Adresse, Locataire, Appartement)
class PersonAdmin(admin.ModelAdmin):
    pass