from django.shortcuts import render
from django.http import HttpResponse

def courses_home(request):
    return render(request, "courses/home.html")

def courses(request):
    return render(request, "courses/courses.html")
