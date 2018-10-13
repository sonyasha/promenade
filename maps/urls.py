from django.urls import include, path
from django.views.generic import TemplateView

from djgeojson.views import GeoJSONLayerView

from paths.models import GeoWalk, SinglePoint, Neighborhood


urlpatterns = [
    path('', TemplateView.as_view(template_name='maps/map.html'), name='map'),
    path('mapdata/', GeoJSONLayerView.as_view(model=GeoWalk, properties=('name', 'description', 'picture_url')), name='mapdata'),
    path('pointsdata/', GeoJSONLayerView.as_view(model=SinglePoint, properties=('name')), name='pointsdata'),
    path('neighborhoodsdata/', GeoJSONLayerView.as_view(model=Neighborhood, properties=('name')), name='neighborhoodsdata'),
]

    