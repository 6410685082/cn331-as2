from django.urls import path
from .views import course, register_course, cancel_registration

urlpatterns = [
    path('', course, name='course_list'),
    path('register/<int:course_id>/', register_course, name='register_course'),
    path('cancel/<int:course_id>/<int:student_id>/', cancel_registration, name='cancel_registration'),
]
