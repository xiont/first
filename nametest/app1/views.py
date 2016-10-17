from django.shortcuts import render,HttpResponse,render_to_response
from models import Test
from models import Login
#from django import forms
from django.db import models
from forms import testForm
from forms import LoginForm
from django.template.context_processors import request
import MySQLdb
#from django.db.transaction import commit
 
#class AddForm(forms.Form):
#    username = forms.CharField(max_length=32)
#    class Meta:
#        model = Test
 
def login(request):
    if request.method=="POST":
        form = testForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            studentnum = form.cleaned_data['studentnum']
            studentmajor = form.cleaned_data['studentmajor']
            test = Test()
            test.username = username
            test.studentnum = studentnum
            test.studentmajor = studentmajor
            test.save()
            return  render(request, 'login.html')
    else:
        form = testForm()
        return render(request, 'login.html')
    
    
def login2(request):
    m = Login.objects.all()
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            idnumber = form.cleaned_data['idnumber']
            home = form.cleaned_data['home']
            if password1 != password2:
                return render(request, 'login2.html')
            else:
                login = Login()
                login.username = username
                login.password1 = password1
                login.password2 = password2
                login.name = name
                login.email = email
                login.idnumber = idnumber
                login.home = home
                login.save()
                #return  render(request, 'login2.html')
                return render_to_response('login2.html',{'m':m})
        else:
            return  HttpResponse("error!")
    else:
        form = LoginForm()
        return render_to_response('login2.html',{'m':m})
        #render(request, 'login2.html')
    
    
def bear(request):
     return render(request, 'test4.html')
     
#def logthen(request):
#    user_list = Test.Objects.all()
#    return render_to_response('logthen.html',{'user_list':user_list})  

#def login(request):
#    if request.method == 'POST':
#        form = AddForm(request.POST)
#        if form.is_valid():
#            username = request.POST['username']
#            Test.objects.create(username=username)
#            return render(request, 'login.html')
#     
#    else:
#        form = AddForm()
#    return render(request, 'login.html')

