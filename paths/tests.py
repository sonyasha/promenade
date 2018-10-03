from django.urls import resolve, reverse
from django.test import TestCase

from paths.views import districts

class DistrictTests(TestCase):
    def test_districts_view_status_code(self):
        url = reverse('districts')
        responce = self.client.get(url)
        self.assertEquals(responce.status_code, 200)

    def test_districts_url_resolves_districts_view(self):
        view = resolve('/districts/')
        print(view.func)
        self.assertEquals(view.func, districts)

class SubdistrictsTests(TestCase):
    def setUp(self):
        District.objects.create(name='New District')

    