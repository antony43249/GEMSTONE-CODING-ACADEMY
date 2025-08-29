from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'age_group_min', 'age_group_max', 'fee', 'mode', 'created_at')
    list_filter = ('level', 'mode')
    search_fields = ('title', 'description')
