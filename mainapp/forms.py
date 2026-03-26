# myapp/forms.py
from django import forms
from .models import Feedback

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()



from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your feedback...', 'rows': 4}),
        }