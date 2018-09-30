from django.urls import path
from paths import views

urlpatterns = [
    path('', views.index, name='index'), # find out ''
    
]
