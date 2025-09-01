from django.http import HttpResponse

def projects_home(request):
    return HttpResponse("<h2>Projects App Home</h2><p>Student project submissions live here.</p>")
