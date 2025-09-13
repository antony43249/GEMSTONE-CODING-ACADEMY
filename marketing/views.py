from django.shortcuts import render
from django.http import HttpResponse

def marketing_home(request):
    return render(request, 'marketing/marketing.html')
