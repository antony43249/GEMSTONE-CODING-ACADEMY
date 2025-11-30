from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, ProfileForm
from .models import Profile
from django.shortcuts import get_object_or_404

def users_home(request):
    return render(request, "users/home.html")

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            messages.success(request, "Account created successfully!")
            return redirect("dashboard-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("dashboard-home")
        else:
            # Provide an interactive error message instead of silent failure
            # Use form.non_field_errors when available for more specific feedback
            err = None
            try:
                err = form.non_field_errors()
            except Exception:
                err = None
            if err:
                messages.error(request, err.as_text())
            else:
                messages.error(request, "Login failed — please check your username and password.")
    else:
        form = UserLoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out.")
    return redirect("users/login")

@login_required
def profile_view(request):
    # ensure a Profile exists for the user; create if missing
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "users/profile.html", {"profile": profile, "created": created})


@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('user-profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_edit.html', {'form': form})
