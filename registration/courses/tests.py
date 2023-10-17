from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Course, Student

# Create your tests here.
class CourseTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='admin', email='admin@test.com')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.course1 = Course.objects.create(name='Course 1', quota=5)
        self.course2 = Course.objects.create(name='Course 2', quota=3)

    def test_register_course_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        response = client.post(f'/courses/register/{self.course1.id}/')
        self.assertRedirects(response, '/courses/enrollment')
        self.assertTrue(Student.objects.filter(user=self.user, courses=self.course1).exists())
        self.assertEqual(Course.objects.get(id=self.course1.id).quota, 4)

    def test_cancel_registration_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        student = Student.objects.create(user=self.user)
        response = client.post(f'/courses/register/{self.course2.id}/')
        self.assertRedirects(response, '/courses/enrollment')
        response = client.post(f'/courses/cancel/{self.course2.id}/{student.id}/')
        self.assertRedirects(response, '/courses/mycourses')
        self.assertFalse(Student.objects.filter(user=self.user, courses=self.course2).exists())
        self.assertEqual(Course.objects.get(id=self.course2.id).quota, 3)

    def test_mycourses_view(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        student = Student.objects.create(user=self.user)
        student.courses.add(self.course1)
        response = client.get('/courses/mycourses')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course 1')
        
    def test_admin_check(self):
        client = Client()
        client.login(username='testuser', password='testpassword')
        student = Student.objects.create(user=self.user)
        student.courses.add(self.course2)
        client.login(username='admin', password='admin')
        response = client.get('/courses/admin_check')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Student.objects.filter(user=self.user).exists())
        self.assertTrue(Student.objects.filter(user=self.user, courses=self.course2).exists())