from djgeojson.fields import MultiLineStringField, PointField, PolygonField, LineStringField

# from gm2m import GM2MField
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import googlemaps

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db.models.signals import pre_save

from promenade.utils import unique_slug_generator
# from paths.google_maps_key import gm_key

# from django.utils.text import slugify



class Neighborhood(models.Model):
    ''' DC neighborhood areas, 5 constant '''
    name = models.CharField(max_length=15)
    geom = PolygonField()
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class SinglePoint(models.Model):
    ''' A single point that can be placed on a map '''
    name = models.CharField(max_length=100)
    geom = PointField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(null=True)

    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    # def add_neighborhood(self):
    #     if not self.checked:
    #         for n in Neighborhood.objects.all():
    #             polygon = Polygon(*(n.geom['coordinates']))
    #             point = Point(*(self.geom['coordinates']))
    #             if polygon.contains(point):
    #                 self.neighborhood = n
    #                 self.checked = True
    #                 self.save()
    #                 break
        

class GeoWalk(models.Model):
    ''' A single walk that can be placed on a map '''
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    # picture = models.ImageField(null=True)
    geom = LineStringField()
    # geom = MultiLineStringField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(null=True)
    slug = models.SlugField(max_length=70, unique=True)

    neighborhood = models.ManyToManyField(Neighborhood, blank=True)
    length_in_meters = models.IntegerField(validators=[MaxValueValidator(20000)], null=True, blank=True)
    length_text = models.CharField(max_length=100, null=True, blank=True)
    duration_in_seconds = models.IntegerField(validators=[MaxValueValidator(86400)], null=True, blank=True)
    duration_text = models.CharField(max_length=100, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = unique_slug_generator(self, self.name, self.slug)
    #     super().save(*args, **kwargs)

    # def add_neighborhoods(self):
    #     if not self.checked:
    #         for n in Neighborhood.objects.all():
    #             polygon = Polygon(*(n.geom['coordinates']))
    #             for coord_pair in self.geom['coordinates']:
    #                 point = Point(coord_pair)
    #                 if polygon.contains(point):
    #                     self.neighborhood.add(n)
    #                     self.checked = True
    #                     self.save()
    #                     break

    # def find_length_duration(self):
    #     if not self.length_in_meters:
    #         gmaps = googlemaps.Client(key=gm_key)
    #         start = f'{self.geom["coordinates"][0][0][1]}, {self.geom["coordinates"][0][0][0]}'
    #         end = f'{self.geom["coordinates"][0][-1][1]}, {self.geom["coordinates"][0][-1][0]}'
    #         try:
    #             results = gmaps.distance_matrix(f'{start}, {end}', mode="walking")
    #             if results:
    #                 try:
    #                     self.length_in_meters = results['rows'][0]['elements'][0]['distance']['value']
    #                     self.length_text = results['rows'][0]['elements'][0]['distance']['text']
    #                     self.duration_in_seconds = results['rows'][0]['elements'][0]['duration']['value']
    #                     self.duration_text = results['rows'][0]['elements'][0]['duration']['text']
    #                     self.save()
    #                 except:
    #                     print('the walk is too long')
    #         except:
    #             print('limit is over')               

    def __str__(self):
        return self.name

def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name, instance.slug)

pre_save.connect(slug_save, sender=GeoWalk)

# class District(models.Model):
#     name = models.CharField(unique=True, max_length=50)
#     slug = models.SlugField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = unique_slug_generator(self, self.name, self.slug)
#         super().save(*args, **kwargs)

# class Subdistrict(models.Model):
#     name = models.CharField(unique=True, max_length=50)
#     district = models.ManyToManyField(District)
#     slug = models.SlugField(max_length=50, unique=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = unique_slug_generator(self, self.name, self.slug)
#         super().save(*args, **kwargs)
    
#     def __str__(self):
#         return self.name

# class Walk(models.Model):
#     name = models.CharField(unique=True, max_length=50, help_text='Enter a name for your Walk (e.g. Southeast Treasure)')
#     description = models.TextField(max_length=150, help_text='Describe the Walk')
#     length = models.DecimalField(decimal_places=1, max_digits=4)
#     duration = models.DecimalField(decimal_places=1, max_digits=4)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(null=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='walks')
#     updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
#     district = models.ManyToManyField(District, help_text='Select a District(s)')
#     subdistrict = models.ManyToManyField(Subdistrict, help_text='Select a Subdistrict(s)')
#     slug = models.SlugField(max_length=100, unique=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = unique_slug_generator(self, self.name, self.slug)
#         super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('walk-detail-view', args=[str(self.id)])

# class Comment(models.Model):
#     message = models.TextField(max_length=2000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     updated_at = models.DateTimeField(null=True)







# class InitialWalk(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=100)
#     geom = MultiLineStringField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class FinalWalk(models.Model):
#     length = models.DecimalField(decimal_places=1, max_digits=4)
#     duration = models.DecimalField(decimal_places=1, max_digits=4)

#     def __str__(self):
#         return self.name




