from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import render_to_string
# from datetime import datetime

from paths.models import District, Subdistrict, Walk, Comment

def districts(request):
    districts = District.objects.all()
    return render(request, 'paths/districts.html', {'first_two': districts[:2], 'second_two': districts[2:]})

def subdistricts(request, slug):
    district = District.objects.get(slug=slug)
    return render(request, 'paths/subdistricts.html', {'district': district})