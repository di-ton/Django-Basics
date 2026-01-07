from profiles.models import Profile


def profile_status(request):
    return {
        'has_profile': Profile.objects.exists()
    }

def profile_processor(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        return {'profile': profile}
    return {'profile': None}