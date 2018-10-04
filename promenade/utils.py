from django.utils.text import slugify
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import ast
# from paths.models import Neighborhood

def unique_slug_generator(model_instance, title, slug_field):
    '''Updates slugs in the existing database'''
    
    slug = slugify(title)

    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():
        # the same as: Walk.objects.filter(slug=slug).exists()

        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug

def define_neighborhood_single_point(model_instance, neighborhood):
    
    all_neighborhoods = neighborhood.objects.all()
    point = Point(model_instance.geom['coordinates'][0])

    for n in all_neighborhoods:
        polygon = Polygon(ast.literal_eval(n.coordinates))
        if polygon.contains(point):
            model_instance.neighborhood.add(n)
            break


