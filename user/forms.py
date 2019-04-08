from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.views.generic import FormView

from user.models import Profile

User = get_user_model()



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Ваш email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Ваш пароль'}))


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


class UserRegistrationForm(forms.Form):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    #name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Укажите имя'}))
    #surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Укажите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Укажите эл.адрес'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Придумайте пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Подтвердите пароль'}))
    #sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'SEX_CHOICES':'value'}))



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



# class AdminRegistrationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email',)
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Пароли не совпадают")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(AdminRegistrationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user




# class UserAdminChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'active', 'admin')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]

