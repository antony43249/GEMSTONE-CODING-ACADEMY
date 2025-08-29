from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'age', 'bio')}),
    )
    list_display = ('username', 'email', 'role', 'age', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
