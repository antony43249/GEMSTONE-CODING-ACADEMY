from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('mentor', 'Mentor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png")
    role = models.CharField(max_length=50, default="Student")  # e.g., Student, Instructor, Admin

    def __str__(self):
        return f"{self.user.username} Profile"

# Auto-create/update profile when user is created
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
