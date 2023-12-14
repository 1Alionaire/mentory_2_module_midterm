from django import forms
from test_app1.models import Feedback

class InputFeedback(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control py-4 textarea-custom', 'placeholder': 'Введите Текст', 'rows': 4
    }))

    class Meta:
        model = Feedback
        fields = ('user_name', 'email', 'message')

