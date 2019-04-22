from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView

from project.decorators import profile_required
from user.forms import UserRegistrationForm, LoginForm, ProfileRegistrationForm
from .models import User, Profile
from trip.models import Trip

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        if request.user.is_authenticated:
            return redirect(reverse('main-page'))
        if request.method == 'POST':
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect(reverse('user-detail'))
            return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect(reverse('main-page'))

@profile_required
def view_profile(request):
    trips = Trip.objects.filter(user=request.user.profile)
    return render(request, 'user/user_detail.html', locals())


def register(request):
    uform = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if uform.is_valid():
            uform.save()
            user = authenticate(email=uform.cleaned_data.get('email'),
                                password=uform.cleaned_data.get('password1'))
            if user:
                login(request, user)
            return redirect(reverse('register-profile-page'))
    return render(request, 'user/register.html', locals())


def register_profile(request):
    pform = ProfileRegistrationForm(request.POST or None)
    if request.method == "POST":
        if  pform.is_valid():
            profile = pform.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Информация о пользователе добавлена')
            return redirect(reverse('main-page'))

    return render(request, 'user/register_profile.html', locals())


def update_profile(request):
    profile = Profile.objects.get(id=request.user.profile.id)
    pform = ProfileRegistrationForm(request.POST, instance=profile)
    # title = 'Обновить данные'
    if request.method == 'POST':
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Данные обновлены')
            return redirect('user-detail')
        else:
            messages.warning(request, '4444')
    return render(request, 'user/update_profile.html', locals())


def confirm_delete(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'user/user_delete.html', locals())


def user_delete(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    messages.info(request, 'Пользователь удален')
    return redirect('main-page')
