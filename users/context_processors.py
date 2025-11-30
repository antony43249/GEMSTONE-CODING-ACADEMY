from .models import Profile

def user_profile(request):
    """Ensure templates have `user_profile` for authenticated users.

    This will create a Profile if missing. Keep lightweight to avoid heavy DB work.
    """
    if not request.user.is_authenticated:
        return {}

    try:
        profile, _ = Profile.objects.get_or_create(user=request.user)
    except Exception:
        # On any unexpected error, avoid crashing templates.
        return {}

    return {"user_profile": profile}
