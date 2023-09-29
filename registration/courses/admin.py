from django.contrib import admin
from .models import Course, Student
from django.contrib.auth.models import User

# Register your models here.
# class StudentInline(admin.TabularInline):
#     model = Student.courses.through

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # inlines = [StudentInline]
    list_display = ['c_name', 'quota']
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal  = ['courses']
