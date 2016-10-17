from django import forms
 
class testForm(forms.Form):
    username = forms.CharField(max_length=32)
    studentnum = forms.IntegerField()
    studentmajor = forms.CharField(max_length=32)
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password1= forms.CharField(max_length=32)
    password2 = forms.CharField(max_length=32)
    email = forms.CharField(max_length=32)
    idnumber = forms.CharField(max_length=32)
    name = forms.CharField(max_length=32)
    home = forms.CharField(max_length=32)