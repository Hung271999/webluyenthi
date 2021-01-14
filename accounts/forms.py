from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(label='Username', max_length=30)
    email=forms.EmailField(label='Email')
    password=forms.CharField(label='Password',widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username=forms.CharField(label='Username', max_length=30)
    password=forms.CharField(label='Password',widget=forms.PasswordInput())