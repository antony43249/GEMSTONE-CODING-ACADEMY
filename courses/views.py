from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Course
from django import forms
from django.contrib import messages


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "age_group_min", "age_group_max", "level", "fee", "mode"]

def courses_home(request):
    return render(request, "courses/home.html")

def courses(request):
    return render(request, "courses/courses.html")


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "courses/detail.html", {"course": course})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            if request.user.is_authenticated:
                course.created_by = request.user
            course.save()
            messages.success(request, "Course created.")
            return redirect("course-detail", pk=course.pk)
    else:
        form = CourseForm()
    return render(request, "courses/create.html", {"form": form})
