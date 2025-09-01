from django.http import HttpResponse

def courses_home(request):
    return HttpResponse("<h2>Courses App Home</h2><p>View and manage courses here.</p>")
