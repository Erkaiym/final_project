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
    #model = User
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'


    def login_form_valid(self, form):
        request = self.request
        if request.user.is_authenticated:
            return redirect(reverse('main-page'))
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
        return super().form_invalid(form)



def logout_view(request):
    logout(request)
    return redirect(reverse('main-page'))

# class RegisterView(FormView):
#     form_class = UserRegistrationForm
#     template_name = 'user/register.html'
#
#     def form_valid(self, form):
#         request = self.request
#         user = User.objects.create_user(email=form.cleaned_data.get('email'),
#                                         password=form.cleaned_data.get('password'))
#         profile = Profile.objects.create_user(name=form.cleaned_data.get('name'))
#         login(request, user, profile)
#         return redirect(reverse('main-page'))


def view_profile(request):
    args = {'user': request.user}
    return render(request, 'user/user_detail.html', args)


def register(request):
    if request.method == 'POST':
        uform = UserRegistrationForm(data = request.POST)
        pform = ProfileRegistrationForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
    return render(request, 'user/register.html', locals())
