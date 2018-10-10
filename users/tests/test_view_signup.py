from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from users.forms import SignUpForm
from users.views import signup
# Create your tests here.

class SignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/account/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

class SuccessfulSignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'eddie',
            'email': 'eddie@somemail.com',
            'password1': '321qwe321',
            'password2': '321qwe321'
        }
        self.response = self.client.post(url, data)
        self.distr_url = reverse('districts')

    def test_redirection(self):
        self.assertRedirects(self.response, self.distr_url)

    def test_user_created(self):
        self.assertTrue(User.objects.exists())

    def test_user_authenticated(self):
        response = self.client.get(self.distr_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTest(TestCase):
    
    def setUp(self):
        url = reverse('signup')
        data = {}
        self.response = self.client.post(url, data)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())