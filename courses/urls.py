from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses_home, name="courses-home"),
    path("courses/", views.courses, name="courses"),
    path("create/", views.course_create, name="course-create"),
    path("<int:pk>/", views.course_detail, name="course-detail"),
]