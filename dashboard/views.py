from django.shortcuts import render
from django.http import HttpResponse

def dashboard_home(request):
    return HttpResponse("<h1>Welcome to Gemstone Coding Academy</h1><p>This is the homepage.</p>")
