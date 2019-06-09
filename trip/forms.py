from django import forms

from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ['user']
        widgets = {
            'start': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Откуда'}),
            'end': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Куда'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Время'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'empty_seats': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество свободных мест'}),

        }

        labels = {
            'start': '',
            'end': '',
            'date': '',
            'time': '',
            'price': '',
            'empty_seats': '',
        }


