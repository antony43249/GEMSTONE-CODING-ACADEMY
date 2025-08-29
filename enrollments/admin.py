from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'progress', 'enrolled_at')
    list_filter = ('status', 'course')
    search_fields = ('student__username', 'course__title')
