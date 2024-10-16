from django import forms
from .models import Panne

class PanneForm(forms.ModelForm):
    class Meta:
        model = Panne
        fields = ['titre', 'description', 'localisation']

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())