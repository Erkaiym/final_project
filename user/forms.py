from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.views.generic import FormView

from user.models import Profile

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder':'Ваш email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Ваш пароль'}))


    def clean_email(self):
        qs = User.objects.filter(email=self.cleaned_data.get('email'))
        if qs.exists() and qs.count() == 1:
            return self.cleaned_data.get('email')
        raise forms.ValidationError('Такого пользователя не существует')


    def clean(self):
        user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        if user:
            return self.cleaned_data
        raise forms.ValidationError('Неверный логин или пароль')


class UserRegistrationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = User
        fields = ['email']
        labels = {
            'email': ''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Укажите эл.адрес'})
        }

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Придумайте пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Подтвердите пароль'}))


    def clean_email(self):
        qs = User.objects.filter(email=self.cleaned_data.get('email'))
        if qs.exists() and qs.count() == 1:
            raise forms.ValidationError('Данный эл.адрес уже используется')
        return self.cleaned_data.get('email')


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'surname', 'sex', 'birthdate', 'tel_number']
        labels = {
            'name':'',
            'surname':'',
            'sex':'Пол',
            'birthdate':'',
            'tel_number':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Укажите имя'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Укажите фамилию'}),
            'birthdate': forms.DateInput(format='%y/%m/%d', attrs={'class': 'datepicker',
                                                                   'placeholder':'Укажите дату рождения (ГГГГ-ММ-ДД'}),
            'sex': forms.RadioSelect(attrs={'SEX_CHOICES':'value'}),
            'tel_number': forms.NumberInput(attrs={'placeholder': 'Укажите номер телефона'})
        }



