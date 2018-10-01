from django.urls import path
from paths import views

urlpatterns = [
    path('', views.index, name='index'),
    path('time/', views.curr_time, name='current_time'),
]
