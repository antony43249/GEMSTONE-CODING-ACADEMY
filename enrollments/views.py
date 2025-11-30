from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Enrollment
from courses.models import Course
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def enrollments_home(request):
    return render(request, "enrollments/home.html")


@login_required
def enrollment_create(request):
    # allow course id via GET or POST
    course_id = request.POST.get("course") or request.GET.get("course")
    if not course_id:
        messages.error(request, "No course chosen for enrollment.")
        return redirect("enrollments-home")

    course = get_object_or_404(Course, pk=course_id)
    # create enrollment
    enrollment = Enrollment.objects.create(student=request.user, course=course)
    messages.success(request, f"Enrolled in {course.title}.")
    return redirect("enrollments-home")
