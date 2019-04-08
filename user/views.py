from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, DetailView, FormView

from user.forms import UserRegistrationForm, LoginForm
from .models import User, Profile

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


class LoginView(FormView):
    #model = User
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'


    def from_valid(self, form):
        request = self.request
        if request.user._is_authenticated:
            return redirect(reverse('main-page'))


# class LogoutView(LogoutView):
#     next_page = 'main-page'


class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        request = self.request
        user = User.objects.create_user(email=form.cleaned_data.get('email'),
                                        password=form.cleaned_data.get('password'))
        login(request, user)
        return redirect(reverse('main-page'))



class UserDetail(DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_user_profile(self, username):
        if self.request.user.is_authenticated:
            return get_object_or_404(User, username=self.request.user)
            #return redirect(reverse('user-detail-page'))



# class UserCreate(CreateView):
#     model = Profile
#     template_name = 'user/user_create.html'
#     fields = '__all__' #['email', 'password', 'password2']
#
#
# class AdminCreate(CreateView):
#     model = User
#     template_name = 'user/admin_create.html'
#     fields = ['email', 'password']





# def user_detail_view(request):
#     context = {
#         'object': request.user,
#     }
#     return render(request, 'user/user_detail.html', context)
#
# def admin_create_view(request):
#     form = UserAdminCreationForm(request.POST or None)
#     return render(request, 'user/admin_create.html', locals())
#
# def user_create_view(request):
#     form = UserCreationForm(request.POST or None)
#     return render(request, 'user/user_create.html', locals())

