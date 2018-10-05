from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from .models import SinglePoint, GeoWalk, Neighborhood

admin.site.register(GeoWalk, LeafletGeoAdmin)
admin.site.register(SinglePoint, LeafletGeoAdmin)
admin.site.register(Neighborhood, LeafletGeoAdmin)

