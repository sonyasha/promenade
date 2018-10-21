from django.test import TestCase
from django.urls import resolve, reverse
from django.test import SimpleTestCase
from django.contrib.auth.models import User

# from ..templatetags import leaflet_tags
from paths.models import Neighborhood, GeoWalk, SinglePoint


# Create your tests here.

class MapDataUrlsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.district = Neighborhood.objects.create(name='New District', geom={"type":"Polygon","coordinates":[[[-77.01756772064958,38.91401270588173],[-77.01644470054677,38.91424038031397],[-76.99067731309495,38.922984764482244],[-76.98540374355869,38.924580016568626],[-76.97739424316825,38.92868609733962],[-76.96349549748187,38.93524604773688],[-76.94444549114694,38.92048790701407],[-76.92194803559413,38.90284934024322],[-76.90933249357992,38.89286541446984],[-76.93364414255991,38.8738697573288],[-76.9397293611171,38.86900263036611],[-76.94679115896449,38.86372632259586],[-76.97374316347495,38.87502874727069],[-76.97930398849596,38.87760402017108],[-76.98457323322508,38.87668958008691],[-76.99115938635487,38.877262298349606],[-77.00057888424202,38.879705979067644],[-77.00065656095119,38.89393184234142],[-77.00072936169909,38.90725964554979],[-77.00446847513915,38.90898444277938],[-77.01186560306972,38.906123769661235],[-77.01201832579397,38.90731548571515],[-77.01392489176823,38.907374860628515],[-77.01618207078499,38.911487978320864],[-77.01756772064958,38.91401270588173]]]}, slug='newdistr')
        self.point = SinglePoint.objects.create(name='New Point', geom={'type':'Point','coordinates':[-77.0153423242,38.920193143]}, created_by=self.user)
        self.walk = GeoWalk.objects.create(name='New Walk', description='New test walk', geom={'type':'LineString','coordinates':[[-77.01024234,38.2001313], [-77.23334566,39.0901092313], [76.992834234,38.64564545345]]}, created_by=self.user)
        self.response = self.client.get('/map/')

    def test_map_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_mapdata_view_status_code(self):
        response = self.client.get('/mapdata/')
        self.assertEquals(self.response.status_code, 200)

    def test_pointdata_view_status_code(self):
        response = self.client.get('/pointsdata/')
        self.assertEquals(self.response.status_code, 200)

    def test_neighborhoodsdata_view_status_code(self):
        response = self.client.get('/neighborhoodsdata/')
        self.assertEquals(self.response.status_code, 200)

    def test_map_container_renders(self):
        self.assertContains(self.response, '<div id="fullmap"',1)
    
