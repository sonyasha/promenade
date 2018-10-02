from django.contrib import admin
from .models import District, Subdistrict, Walk, Comment

admin.site.register(District)
admin.site.register(Subdistrict)
admin.site.register(Walk)
admin.site.register(Comment)