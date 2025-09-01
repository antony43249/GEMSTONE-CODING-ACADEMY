from django.http import HttpResponse

def marketing_home(request):
    return HttpResponse("<h2>Marketing App Home</h2><p>Blog, events, and campaigns live here.</p>")
