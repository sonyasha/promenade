from djgeojson.fields import MultiLineStringField
from djgeojson.fields import PointField
from djgeojson.fields import PolygonField
from gm2m import GM2MField

from django.db import models
from django.contrib.auth.models import User

from promenade.utils import unique_slug_generator
from promenade.utils import define_neighborhood_single_point
# from django.utils.text import slugify

class District(models.Model):
    name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name, self.slug)
        super().save(*args, **kwargs)

class Subdistrict(models.Model):
    name = models.CharField(unique=True, max_length=50)
    district = models.ManyToManyField(District)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name, self.slug)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Walk(models.Model):
    name = models.CharField(unique=True, max_length=50, help_text='Enter a name for your Walk (e.g. Southeast Treasure)')
    description = models.TextField(max_length=150, help_text='Describe the Walk')
    length = models.DecimalField(decimal_places=1, max_digits=4)
    duration = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='walks')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
    district = models.ManyToManyField(District, help_text='Select a District(s)')
    subdistrict = models.ManyToManyField(Subdistrict, help_text='Select a Subdistrict(s)')
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self, self.name, self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('walk-detail-view', args=[str(self.id)])

class Comment(models.Model):
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)

class Neighborhood(models.Model):
    ''' DC neighborhood areas, 5 constant '''
    name = models.CharField(max_length=15)
    coordinates = models.TextField(null=True)
    # geom = PolygonField()
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class SinglePoint(models.Model):
    ''' A single point that can be placed on a map '''
    name = models.CharField(max_length=100)
    geom = PointField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        define_neighborhood_single_point(self, Neighborhood)
        super().save(*args, **kwargs)


class GeoWalk(models.Model):
    ''' A single walk  that can be placed on a map '''
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    # picture = models.ImageField(null=True)
    geom = MultiLineStringField()
    neighborhood = models.ManyToManyField(Neighborhood, null=True)
    

    def __str__(self):
        return self.name

    # @property
    # def picture_url(self):
    #     return self.picture.url


