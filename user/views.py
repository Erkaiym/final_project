from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django import forms
from django.views.generic import CreateView, DetailView, FormView, UpdateView


from user.forms import UserRegistrationForm, LoginForm, ProfileRegistrationForm
from .models import User, Profile

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


def view_profile(request):
    return render(request, 'user/user_detail.html', {'user': request.user})


def register(request):
    uform = UserRegistrationForm(data = request.POST)
    if uform.is_valid():
        uform.save()
        return redirect(reverse('login-page'))
    return render(request, 'user/register.html', locals())


def register_profile(request):
    pform = ProfileRegistrationForm(data=request.POST)
    if  pform.is_valid():
        profile = pform.save(commit=False)
        profile.user = request.user
        profile.save()
        messages.success(request, 'Информация о пользователе добавлена.')
        return redirect(reverse('main-page'))
    return render(request, 'user/register_profile.html', locals())

