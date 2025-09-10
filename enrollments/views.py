from django.shortcuts import render
from django.http import HttpResponse

def enrollments_home(request):
    return render(request, "enrollments/home.html")
