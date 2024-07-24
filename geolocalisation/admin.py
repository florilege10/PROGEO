from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
from .models import *

class vehecules(LeafletGeoAdmin):

    pass

# Register your models here.
admin.site.register(Voiture, vehecules)
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Chauffeur)
##admin.site.registega r./u90r(Conduire)
admin.site.register(Commander)
admin.site.register(Location)