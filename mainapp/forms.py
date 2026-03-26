# myapp/forms.py
from django import forms
from .models import Feedback

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name', 'email',
            'accommodation', 'travel', 'food', 'registration',
            'talks_and_discussions', 'venue', 'overall_experience',
            'message'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }