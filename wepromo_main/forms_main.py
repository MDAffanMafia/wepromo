from django import forms

class SignUp(forms.Form):
    userName=forms.CharField()
    email=forms.EmailField()
    