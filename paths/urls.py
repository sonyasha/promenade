from django.urls import path
from paths import views


urlpatterns = [
    path('', views.districts, name='districts'),
    path('<slug>/', views.district_walks, name='district_walks'),
    path('<slug>/new_walk/', views.new_walk, name='new_walk'),
    path('<slug>/<walk_slug>/', views.single_walk, name='single_walk'),
]
