from django.http import HttpResponse

def payments_home(request):
    return HttpResponse("<h2>Payments App Home</h2><p>Manage tuition and sponsorship payments here.</p>")
