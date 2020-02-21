from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
