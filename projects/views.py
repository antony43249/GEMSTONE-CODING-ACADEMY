from django.shortcut import render
from django.http import HttpResponse

def projects_home(request):
    return render(request, 'projects/home.html')
