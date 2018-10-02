from django.db import models
from django.contrib.auth.models import User

class District(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name

class Subdistrict(models.Model):
    name = models.CharField(unique=True, max_length=50)
    district = models.ManyToManyField(District)
    
    def __str__(self):
        return self.name

class Walk(models.Model):
    name = models.CharField(unique=True, max_length=50, help_text='Enter a name for your Walk (e.g. Southeast Treasure)')
    description = models.TextField(max_length=2000, help_text='Describe the Walk')
    length = models.DecimalField(decimal_places=1, max_digits=4)
    duration = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='walks')
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
    district = models.ManyToManyField(District, help_text='Select a District(s)')
    subdistrict = models.ManyToManyField(Subdistrict, help_text='Select a Subdistrict(s)')
    slug = models.SlugField(max_length=50, unique=True)

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

