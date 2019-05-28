from django import forms


from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['user', 'created_at', 'profile', 'trip']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Укажите имя'},
            'tel_number': forms.NumberInput(attrs={'placeholder': 'Укажите номер телефона'},
        }