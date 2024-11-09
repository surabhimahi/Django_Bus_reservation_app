from django import forms
# from Bus_reservations.myforms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RouteForm (forms.ModelForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    class Meta:
        model = Route
        fields =['start_route','end_route']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name']
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
    
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields =('username', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)