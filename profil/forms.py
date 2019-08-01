from django import forms
from django.forms import PasswordInput,TextInput
from .models import utilisateur


class LoginForm(forms.ModelForm):

    class Meta:
        model = utilisateur
        fields = ('username', 'password')
        widgets ={
            'password': PasswordInput(attrs={'class':'form-control mb-4 validate'}),
            'username':TextInput(attrs={'class':'form-control  validate'})}

class New_userForm(forms.ModelForm):
    class Meta:
        model = utilisateur 
        fields= ('username','mail','password')
        widgets ={
            'password': PasswordInput(attrs={'class':'form-control mb-4 validate'}),
            'username':TextInput(attrs={'class':'form-control  validate'}),
            'mail':TextInput(attrs={'class':'form-control mb-4 validate'})}

