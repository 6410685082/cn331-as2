from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    c_name = models.CharField(max_length=100)
    quota = models.IntegerField(default=40)
    def __str__(self):
        return f"{self.c_name} ({self.quota})"

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course, blank=True, related_name='students')
    def __str__(self):
        return f"{self.user} : {self.name}"