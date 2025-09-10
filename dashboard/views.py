from django.shortcuts import render
from django.http import HttpResponse

def dashboard_home(request):
    return render(request, "dashboard/home.html")
