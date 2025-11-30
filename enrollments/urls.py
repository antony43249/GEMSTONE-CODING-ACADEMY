from django.urls import path
from . import views

urlpatterns = [
    path("", views.enrollments_home, name="enrollments-home"),
    path("create/", views.enrollment_create, name="enrollment-create"),
]
