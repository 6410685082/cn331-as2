from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import Course, Student

@login_required
def course_list(request):
    courses = Course.objects.all()
    user = request.user
    registrations = Student.objects.filter(user=user, courses__in=courses)
    registered_courses = registrations[0].courses.all() if len(registrations) != 0 else []

    return render(request, 'courses/course.html', {'courses': courses, 'registrations': registered_courses, 'user': user})

@login_required
def register_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    user = request.user

    if not Student.objects.filter(user=user, courses=course).exists() and course.quota > 0:
        student, created = Student.objects.get_or_create(user=user)
        course.students.add(student)
        course.quota -= 1
        course.save()

    return redirect('course_list')

@login_required
def cancel_registration(request, course_id, student_id):
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=student_id)

    if student.user == request.user:
        course.students.remove(student)
        course.quota += 1
        course.save()

    return redirect('my_courses')

@login_required
def my_courses(request):
    user = request.user
    student = Student.objects.get(user=user)
    registered_courses = student.courses.all()
    
    return render(request, 'courses/mycourses.html', {'registered_courses': registered_courses})

@staff_member_required
def admin_check(request):
    all_students = Student.objects.all()
    
    return render(request, 'courses/admin_check.html', {'all_students': all_students})

        