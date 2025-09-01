from django.http import HttpResponse

def dashboard_home(request):
    return HttpResponse("<h2>Dashboard Home</h2><p>Analytics and reports live here.</p>")
