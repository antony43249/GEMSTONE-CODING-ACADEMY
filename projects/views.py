from django.shortcuts import render
from django.http import HttpResponse

def projects_home(request):
    return render(request, 'projects/projects.html')
