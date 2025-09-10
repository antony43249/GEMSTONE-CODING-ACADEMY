from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses_home, name="courses-home"),
    path("courses/", views.courses, name="courses"),
]