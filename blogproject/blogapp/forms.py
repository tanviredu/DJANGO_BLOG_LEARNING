from django import forms 




class LoginForm(forms.Form):
    user = forms.CharField(max_length=150)
    user = forms.CharField(widget = forms.PasswordInput())