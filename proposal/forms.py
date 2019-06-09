from django import forms


from .models import Proposal


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        exclude = ['created_at', 'profile', 'trip', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Подтвердите имя'}),
            'tel_number': forms.NumberInput(attrs={'placeholder': 'Подтвердите номер телефона'}),
        }

        labels = {
            'name': '',
            'tel_number': '',
        }


    def __init__(self, *args, **kwargs):
        self._name = kwargs['name']
        del kwargs['name']
        super().__init__(*args, **kwargs)


    def save(self, commit=True):
        proposal = super().save(commit=False)
        proposal.name = self._name
        proposal.save()
        return proposal


