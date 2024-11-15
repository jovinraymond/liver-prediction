from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import LiverCirrhosisPrediction

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.home_url = reverse('home')
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.retrieval_url = reverse('retrieval')

    def test_home_page_requires_login(self):
        response = self.client.get(self.home_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.home_url}')

    def test_home_page_access_logged_in(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_signup_page(self):
        response = self.client.post(self.signup_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after signup
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_signup_page_invalid_email(self):
        response = self.client.post(self.signup_url, {
            'username': 'invaliduser',
            'email': 'invalid-email',
            'password1': 'Password123!',
            'password2': 'Password123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Invalid email format", response.content)

    def test_login_page_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'pass': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertRedirects(response, self.home_url)

    def test_login_page_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'pass': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password is incorrect', response.content)

    def test_logout_page(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.logout_url)
        self.assertRedirects(response, self.login_url)

    def test_retrieval_page_requires_login(self):
        response = self.client.get(self.retrieval_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.retrieval_url}')

    def test_retrieval_page_access_logged_in(self):
        self.client.login(username='testuser', password='password123')
        LiverCirrhosisPrediction.objects.create(
            n_days=1, hepatomegaly=1, albumin=1, platelets=1, prothrombin=1, status=1, prediction=1
        )
        response = self.client.get(self.retrieval_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'retrieval.html')
        self.assertContains(response, 'Prediction')

