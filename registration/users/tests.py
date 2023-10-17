from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_pass_login(self):
        client = Client()
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = client.post('/users/login', data = data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/users/')
        
    def test_wrong_login(self):
        client = Client()
        data = {'username': 'amumunu', 'password': 'password123'}
        response = client.post('/users/login', data = data)
        self.assertEqual(response.status_code, 200)
        
    def test_get_login_page(self):
        client = Client()
        response = client.get('/users/login')
        self.assertEqual(response.status_code, 200)
        
    def test_logout(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post('/users/logout')
        self.assertEqual(response.status_code, 200)
        
    def test_pass_main(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.get('/users/')
        self.assertEqual(response.status_code, 200)
    
    def test_without_login_main(self):
        client = Client()
        response = client.get('/users/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/users/login')