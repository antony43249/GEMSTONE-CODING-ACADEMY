from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects_home, name="projects-home"),
    path("create/", views.project_create, name="project-create"),
    path("<int:pk>/", views.project_detail, name="project-detail"),
]
