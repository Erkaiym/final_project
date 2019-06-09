from django import forms


from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'created_at']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}),
        }

        labels = {
            'comment': '',
        }
