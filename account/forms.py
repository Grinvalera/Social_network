from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import User, PictureUser


class LoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number']

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] == cd['password2']:
            return cd['password2']
        else:
            raise forms.ValidationError('Password don\'t match.')


class UploadPicture(ModelForm):
    class Meta:
        model = PictureUser
        exclude = []

