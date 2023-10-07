from django.urls import path
from .views import course_list, register_course, cancel_registration, my_courses, admin_check

urlpatterns = [
    path('register/<int:course_id>/', register_course, name='register_course'),
    path('cancel/<int:course_id>/<int:student_id>/', cancel_registration, name='cancel_registration'),
    path('enrollment', course_list, name='course_list'),
    path('mycourses', my_courses, name='my_courses'),
    path('admin_check', admin_check, name='admin_check'),
]
