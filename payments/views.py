from django.shortcuts import render
from django.http import HttpResponse

def payments_home(request):
    return render(request, 'payments/home.html')
