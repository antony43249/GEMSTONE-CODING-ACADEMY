from django.db import models
from users.models import User

class Course(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    age_group_min = models.PositiveIntegerField()
    age_group_max = models.PositiveIntegerField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    mode = models.CharField(max_length=20, choices=[('online', 'Online'), ('offline', 'Offline')])
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_courses")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.level})"
