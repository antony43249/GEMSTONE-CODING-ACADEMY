from django.urls import path
from .views import register_view, login_view, logout_view
from .import views

urlpatterns = [
    path("", views.users_home, name="users-home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", views.profile_view, name="user-profile"),
]
