from django import forms

class loginForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 't', 'placeholder': 'Name'}),label='')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={ 'id': 'pass', 'placeholder': 'Password'}),label='')
class requet(forms.Form):
    req = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 'req', 'placeholder': 'Requête'}),label='')
class result(forms.Form):
    rslt= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id' : 'rslt', 'placeholder': 'rslt'}),label='')

 