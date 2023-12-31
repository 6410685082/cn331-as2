from django.contrib import admin
from .models import Course, Student

# Register your models here.
# class StudentInline(admin.TabularInline):
#     model = Student.courses.through

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # inlines = [StudentInline]
    list_display = ['name','num', 'sem', 'year', 'quota', 'open']
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    filter_horizontal  = ['courses']
