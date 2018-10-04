from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from .models import District, Subdistrict, Walk, Comment, SinglePoint, GeoWalk, Neighborhood

admin.site.register(District)
admin.site.register(Subdistrict)
admin.site.register(Walk)
admin.site.register(Comment)
admin.site.register(GeoWalk, LeafletGeoAdmin)
admin.site.register(SinglePoint, LeafletGeoAdmin)
admin.site.register(Neighborhood, LeafletGeoAdmin)