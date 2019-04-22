from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from user.models import Profile


def profile_required(some_function):
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            if Profile.objects.filter(user=user).exists():
                return some_function(request, *args, **kwargs)
            else:
                return redirect('register-profile-page')
        else:
            return redirect('login-page')
    return wrapper
