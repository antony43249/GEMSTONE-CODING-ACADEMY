from django.http import HttpResponse

def enrollments_home(request):
    return HttpResponse("<h2>Enrollments App Home</h2><p>Students enroll into courses here.</p>")
