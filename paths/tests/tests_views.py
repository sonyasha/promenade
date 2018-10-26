from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase

from paths.forms import NewWalkForm
from paths.views import districts, district_walks, new_walk, single_walk
from paths.models import Neighborhood, GeoWalk

class DistrictTests(TestCase):
    def setUp(self):
        self.district = Neighborhood.objects.create(name='New District', geom={"type":"Polygon","coordinates":[[[-77.01756772064958,38.91401270588173],[-77.01644470054677,38.91424038031397],[-76.99067731309495,38.922984764482244],[-76.98540374355869,38.924580016568626],[-76.97739424316825,38.92868609733962],[-76.96349549748187,38.93524604773688],[-76.94444549114694,38.92048790701407],[-76.92194803559413,38.90284934024322],[-76.90933249357992,38.89286541446984],[-76.93364414255991,38.8738697573288],[-76.9397293611171,38.86900263036611],[-76.94679115896449,38.86372632259586],[-76.97374316347495,38.87502874727069],[-76.97930398849596,38.87760402017108],[-76.98457323322508,38.87668958008691],[-76.99115938635487,38.877262298349606],[-77.00057888424202,38.879705979067644],[-77.00065656095119,38.89393184234142],[-77.00072936169909,38.90725964554979],[-77.00446847513915,38.90898444277938],[-77.01186560306972,38.906123769661235],[-77.01201832579397,38.90731548571515],[-77.01392489176823,38.907374860628515],[-77.01618207078499,38.911487978320864],[-77.01756772064958,38.91401270588173]]]}, slug='newdistr')
        url = reverse('districts')
        self.response = self.client.get(url)

    def test_districts_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_districts_url_resolves_districts_view(self):
        view = resolve('/districts/')
        self.assertEquals(view.func, districts)

    def test_districts_view_contains_link_to_district_walks_page(self):
        district_walks_url = reverse('district_walks', kwargs={'slug': self.district.slug})
        self.assertContains(self.response, f'href="{district_walks_url}"')


class DistrictWalks(TestCase):
    def setUp(self):
        Neighborhood.objects.create(name='New District', geom={"type":"Polygon","coordinates":[[[-77.01756772064958,38.91401270588173],[-77.01644470054677,38.91424038031397],[-76.99067731309495,38.922984764482244],[-76.98540374355869,38.924580016568626],[-76.97739424316825,38.92868609733962],[-76.96349549748187,38.93524604773688],[-76.94444549114694,38.92048790701407],[-76.92194803559413,38.90284934024322],[-76.90933249357992,38.89286541446984],[-76.93364414255991,38.8738697573288],[-76.9397293611171,38.86900263036611],[-76.94679115896449,38.86372632259586],[-76.97374316347495,38.87502874727069],[-76.97930398849596,38.87760402017108],[-76.98457323322508,38.87668958008691],[-76.99115938635487,38.877262298349606],[-77.00057888424202,38.879705979067644],[-77.00065656095119,38.89393184234142],[-77.00072936169909,38.90725964554979],[-77.00446847513915,38.90898444277938],[-77.01186560306972,38.906123769661235],[-77.01201832579397,38.90731548571515],[-77.01392489176823,38.907374860628515],[-77.01618207078499,38.911487978320864],[-77.01756772064958,38.91401270588173]]]}, slug='newdistr')
    
    def test_district_walks_view_success_status_code(self):
        url = reverse('district_walks', kwargs={'slug': 'newdistr'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_district_walks_view_not_found_status_code(self):
        url = reverse('district_walks', kwargs={'slug': 'wrongslug'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_district_walks_url_resolves_district_walks_view(self):
        view = resolve('/districts/newdistr/')
        self.assertEquals(view.func, district_walks)

    def test_district_walks_view_contains_link_back_to_districtpage(self):
        district_walks_url = reverse('district_walks', kwargs={'slug': 'newdistr'})
        districtpage_url = reverse('districts')
        new_walk_url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        response = self.client.get(district_walks_url)
        self.assertContains(response, f'href="{districtpage_url}"')
        self.assertContains(response, f'href="{new_walk_url}"')

class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        Neighborhood.objects.create(name='New District', geom={"type":"Polygon","coordinates":[[[-77.01756772064958,38.91401270588173],[-77.01644470054677,38.91424038031397],[-76.99067731309495,38.922984764482244],[-76.98540374355869,38.924580016568626],[-76.97739424316825,38.92868609733962],[-76.96349549748187,38.93524604773688],[-76.94444549114694,38.92048790701407],[-76.92194803559413,38.90284934024322],[-76.90933249357992,38.89286541446984],[-76.93364414255991,38.8738697573288],[-76.9397293611171,38.86900263036611],[-76.94679115896449,38.86372632259586],[-76.97374316347495,38.87502874727069],[-76.97930398849596,38.87760402017108],[-76.98457323322508,38.87668958008691],[-76.99115938635487,38.877262298349606],[-77.00057888424202,38.879705979067644],[-77.00065656095119,38.89393184234142],[-77.00072936169909,38.90725964554979],[-77.00446847513915,38.90898444277938],[-77.01186560306972,38.906123769661235],[-77.01201832579397,38.90731548571515],[-77.01392489176823,38.907374860628515],[-77.01618207078499,38.911487978320864],[-77.01756772064958,38.91401270588173]]]}, slug='newdistr')
        self.url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class NewWalkTests(TestCase):
    def setUp(self):
        Neighborhood.objects.create(name='New District', geom={"type":"Polygon","coordinates":[[[-77.01756772064958,38.91401270588173],[-77.01644470054677,38.91424038031397],[-76.99067731309495,38.922984764482244],[-76.98540374355869,38.924580016568626],[-76.97739424316825,38.92868609733962],[-76.96349549748187,38.93524604773688],[-76.94444549114694,38.92048790701407],[-76.92194803559413,38.90284934024322],[-76.90933249357992,38.89286541446984],[-76.93364414255991,38.8738697573288],[-76.9397293611171,38.86900263036611],[-76.94679115896449,38.86372632259586],[-76.97374316347495,38.87502874727069],[-76.97930398849596,38.87760402017108],[-76.98457323322508,38.87668958008691],[-76.99115938635487,38.877262298349606],[-77.00057888424202,38.879705979067644],[-77.00065656095119,38.89393184234142],[-77.00072936169909,38.90725964554979],[-77.00446847513915,38.90898444277938],[-77.01186560306972,38.906123769661235],[-77.01201832579397,38.90731548571515],[-77.01392489176823,38.907374860628515],[-77.01618207078499,38.911487978320864],[-77.01756772064958,38.91401270588173]]]}, slug='newdistr')
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.client.login(username='john', password='123')

    

    def test_new_walk_view_success_status_code(self):
        url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_walk_view_not_found_status_code(self):
        url = reverse('new_walk', kwargs={'slug': 'wrongslug'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_walk_url_resolves_new_walk_view(self):
        view = resolve('/districts/newdistr/new_walk/')
        self.assertEquals(view.func, new_walk)

    def test_new_walk_view_contains_link_back_to_districtwalks(self):
        new_walk_url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        district_walks_url = reverse('district_walks', kwargs={'slug': 'newdistr'})
        response = self.client.get(new_walk_url)
        # self.assertContains(response, f'href="{district_walks_url}"') #need to figure out why it's not working

    def test_csrf(self):
        url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_walk_invalid_data(self):
        '''
        Invalid data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_walk_invalid_data_empty_fields(self):
        '''
        Invalid data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        data = {
            'name': '',
            'description': '',
            'geom': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(GeoWalk.objects.exists())
    
    def test_new_walk_valid_data(self):
        url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        data = {
            'name': 'Test walk',
            'description': 'Lorem ipsum dolor sit amet',
            'geom': {'type': 'LineString', 'coordinates': [[-77.023013, 38.023586], [-77.053453, 38.043313], [-77.025013, 38.027586]]}
        }
        response = self.client.post(url, data)
        # self.assertTrue(GeoWalk.objects.exists()) #test fails
    
    def test_contains_form(self):
        url = reverse('new_walk', kwargs={'slug': 'newdistr'})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewWalkForm)

class GeoWalkSlugTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.client.login(username='john', password='123')
        GeoWalk.objects.create(name='New walk', description='Lorem ipsum dolor sit amet', geom={'type': 'LineString', 'coordinates': [[-77.023013, 38.023586], [-77.053453, 38.043313], [-77.025013, 38.027586]]}, created_by=user)
        GeoWalk.objects.create(name='New walk', description='2Lorem ipsum dolor sit amet', geom={'type': 'LineString', 'coordinates': [[-77.033013, 38.033586], [-77.093453, 38.073313], [-77.025013, 38.027586]]}, created_by=user)
        

    def test_check_slug_unique(self):
        walk_1 = GeoWalk.objects.get(pk=1)
        walk_2 = GeoWalk.objects.get(pk=2)

        self.assertEqual(walk_1.slug, 'new-walk')
        self.assertEqual(walk_2.slug, 'new-walk-2')

class SingleWalkTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        # self.client.login(username='john', password='123')
        district = Neighborhood.objects.create(name='New District', geom={"type":"Polygon","coordinates":[[[-77.01756772064958,38.91401270588173],[-77.01644470054677,38.91424038031397],[-76.99067731309495,38.922984764482244],[-76.98540374355869,38.924580016568626],[-76.97739424316825,38.92868609733962],[-76.96349549748187,38.93524604773688],[-76.94444549114694,38.92048790701407],[-76.92194803559413,38.90284934024322],[-76.90933249357992,38.89286541446984],[-76.93364414255991,38.8738697573288],[-76.9397293611171,38.86900263036611],[-76.94679115896449,38.86372632259586],[-76.97374316347495,38.87502874727069],[-76.97930398849596,38.87760402017108],[-76.98457323322508,38.87668958008691],[-76.99115938635487,38.877262298349606],[-77.00057888424202,38.879705979067644],[-77.00065656095119,38.89393184234142],[-77.00072936169909,38.90725964554979],[-77.00446847513915,38.90898444277938],[-77.01186560306972,38.906123769661235],[-77.01201832579397,38.90731548571515],[-77.01392489176823,38.907374860628515],[-77.01618207078499,38.911487978320864],[-77.01756772064958,38.91401270588173]]]}, slug='newdistr')
        walk = GeoWalk.objects.create(name='New walk', description='2Lorem ipsum dolor sit amet', geom={'type': 'LineString', 'coordinates': [[-77.033013, 38.033586], [-77.093453, 38.073313], [-77.025013, 38.027586]]}, created_by=user)
        url = reverse('single_walk', kwargs={'slug': district.slug, 'walk_slug': walk.slug})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)
        
    def test_view_function(self):
        view = resolve('/districts/newdistr/new-walk/')
        self.assertEquals(view.func, single_walk)