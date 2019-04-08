from django import forms
from django.contrib.auth import get_user_model, authenticate

from user.models import Profile

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваш логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ваш пароль'}))


    def clean_username(self):
        qs = User.objects.filter(username=self.cleaned_data.get('username'))
        if qs.exists() and qs.count() ==1:
            return self.cleaned_data.get('username')
        raise forms.ValidationError('Пользователя с таким логином не существует')

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user:
            return self.cleaned_data.get('password')
        raise forms.ValidationError('Неверный логин или пароль')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname']

        widgets = {
            #'username': forms.TextInput(attrs={'placeholder':'Логин'}),
            'name': forms.TextInput(attrs={'placeholser':'Имя'}),
            'surname': forms.TextInput(attrs={'placeholder':'Фамилия'}),
            #'email': forms.EmailInput(attrs={'placeholder':'Электронный адрес'}),
            #'password': forms.PasswordInput(attrs={'placeholder':'Повторите пароль'}),
        }



        # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Логин'}))
        # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Имя'}))
        # surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Фамилия'}))
        # #birthdate
        # #choices
        # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Электронный адрес'}))
        # #tel_number
        # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
        # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Повторите пароль'}))

