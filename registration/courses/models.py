from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    c_name = models.CharField(max_length=32)
    quota = models.IntegerField(default=40)
    def __str__(self):
        return f"{self.c_name} ({self.quota})"

class Student(models.Model):
    # name = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, related_name='students')
    def __str__(self):
        return f"{self.user} : {self.courses}"
    