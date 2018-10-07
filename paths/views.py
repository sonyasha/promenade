from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django import template
from django.template.loader import render_to_string
# from datetime import datetime

from paths.forms import NewWalkForm
from paths.models import Neighborhood, SinglePoint, GeoWalk

def districts(request):
    districts = Neighborhood.objects.all()
    return render(request, 'paths/districts.html', {'districts': districts})

def district_walks(request, slug):
    district = get_object_or_404(Neighborhood, slug=slug)
    walks = GeoWalk.objects.filter(neighborhood=district.id)
    return render(request, 'paths/district_walks.html', {'district': district, 'walks': walks})

def new_walk(request, slug):
    district = get_object_or_404(Neighborhood, slug=slug)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewWalkForm(request.POST)
        if form.is_valid():
            walk = form.save(commit=False)
            walk.created_by = user
            walk = form.save()
            print(walk.geom)
            return redirect('district_walks', slug=district.slug)
    else:
        form = NewWalkForm()
    return render(request, 'paths/new_walk.html', {'district': district, 'form': form})

