from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.forms import ModelForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

class RegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(ModelForm, self).__init__(*args, **kwargs)
    #
    #     for key, field in self.fields.items():
    #         field.widget.attrs.update({"class": "input input--text"})