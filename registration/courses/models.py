from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=64)
    num = models.CharField(max_length=16)
    sem = models.CharField(max_length=4)
    year = models.CharField(max_length=8)
    quota = models.IntegerField(default=40)
    open = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} ({self.num}) : ({self.quota}) ({self.sem})/({self.year})"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, related_name='students')
    def __str__(self):
        return f"{self.user} : {self.courses.name}"
    