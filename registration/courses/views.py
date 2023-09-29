from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course, Student
from django.urls import reverse


# Create your views here.
def course(request):
    courses = Course.objects.all()
    return render(request, 'courses/course.html', {'courses': courses})

def register_course(request, course_id):
    course = Course.objects.get(pk=course_id)

    if course.quota > 0:
        student = Student(name="Not adding")
        student.save()
        course.students.add(student)
        course.quota -= 1
        course.save()

    return HttpResponseRedirect(reverse('course'))

def cancel_registration(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)

    course.students.remove(student)
    course.quota += 1
    course.save()

    return HttpResponseRedirect(reverse('course'))