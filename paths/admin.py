from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from .models import SinglePoint, GeoWalk, Neighborhood


class NewLeafletGeoAdmin(LeafletGeoAdmin):
    map_height = '550px'

    list_display = ['name', 'created_by', 'created_at', 'checked']
    actions = ['add_neighborhood', ]

    def add_neighborhood(self, request, queryset):
        for element in queryset:
            if not element.checked:
                for n in Neighborhood.objects.all():
                    polygon = Polygon(*(n.geom['coordinates']))
                    if element.geom['type'] == 'Point':
                        point = Point(*(element.geom['coordinates']))
                        if polygon.contains(point):
                            element.neighborhood = n
                            element.checked = True
                            element.save()
                            break
                    elif element.geom['type'] == 'LineString':
                        for coord_pair in element.geom['coordinates']:
                            point = Point(coord_pair)
                            if polygon.contains(point):
                                element.neighborhood.add(n)
                                element.checked = True
                                element.save()
                                break


admin.site.register(GeoWalk, NewLeafletGeoAdmin)
admin.site.register(SinglePoint, NewLeafletGeoAdmin)
admin.site.register(Neighborhood, LeafletGeoAdmin)

