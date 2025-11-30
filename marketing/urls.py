from django.urls import path
from . import views

urlpatterns = [
    path("", views.marketing_home, name="marketing-home"),
    path("create/", views.marketing_create, name="marketing-create"),
    path("<int:pk>/", views.marketing_detail, name="marketing-detail"),
]
