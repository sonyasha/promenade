from django.test import TestCase
from django.urls import resolve, reverse
from users.views import signup
# Create your tests here.

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/account/signup/')
        self.assertEquals(view.func, signup)