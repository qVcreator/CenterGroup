from django import forms

from .models import *


class FeedbackForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    PhoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телфона'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'text': forms.Textarea(attrs={'placeholder': 'Комментарий'}),
        }
