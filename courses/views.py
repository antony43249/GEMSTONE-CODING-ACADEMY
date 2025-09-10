from django.shortcurt import render
from django.http import HttpResponse

def courses_home(request):
    return render(request, "home.html")
