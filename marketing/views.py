from django.shortcurt import render
from django.http import HttpResponse

def marketing_home(request):
    return render(request, 'marketing/home.html')
