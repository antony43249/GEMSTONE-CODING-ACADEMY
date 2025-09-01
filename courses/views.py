from django.shortcuts import render
from django.http import HttpResponse

def users_home(request):
    return HttpResponse("<h2>Users App Home</h2><p>Manage authentication and profiles here.</p>")
