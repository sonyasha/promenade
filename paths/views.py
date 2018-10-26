from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import Http404
from django import template
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# from datetime import datetime

from paths.forms import NewWalkForm
from paths.models import Neighborhood, SinglePoint, GeoWalk

def districts(request):
    districts = Neighborhood.objects.order_by('name')
    return render(request, 'paths/districts.html', {'districts': districts})

def district_walks(request, slug):
    district = get_object_or_404(Neighborhood, slug=slug)
    walks = GeoWalk.objects.filter(neighborhood=district.id).order_by('name', 'created_at')
    return render(request, 'paths/district_walks.html', {'district': district, 'walks': walks})

@login_required
def new_walk(request, slug):
    district = get_object_or_404(Neighborhood, slug=slug)
    # user = User.objects.first()
    if request.method == 'POST':
        form = NewWalkForm(request.POST)
        if form.is_valid():
            walk = form.save(commit=False)
            walk.created_by = request.user
            walk = form.save()
            # print(walk.geom)
            return redirect('district_walks', slug=district.slug)
    else:
        form = NewWalkForm()
    return render(request, 'paths/new_walk.html', {'district': district, 'form': form})

def single_walk(request, slug, walk_slug):
    walk = get_object_or_404(GeoWalk, slug=walk_slug)
    district = get_object_or_404(Neighborhood, slug=slug)
    return render(request, 'paths/single_walk.html', {'district': district, 'walk': walk})

# @login_required
# def new_walk(request):
#     districts = Neighborhood.objects.order_by('name')
#     user = User.objects.first()
#     if request.method == 'POST':
#         form = NewWalkForm(request.POST)
#         if form.is_valid():
#             walk = form.save(commit=False)
#             walk.created_by = request.user
#             walk = form.save()
#             # print(walk.geom)
#             return render(request, 'paths/districts.html', {'districts': districts})
#     else:
#         form = NewWalkForm()
#     return render(request, 'paths/new_walk.html', {'form': form})

