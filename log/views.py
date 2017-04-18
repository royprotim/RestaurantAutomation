#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")
	'''return HttpResponse("<h1>welcome to home page</h1>")'''

def detail(request):
	return render(request,"detail.html")

def aboutus(request):
	return render(request,"aboutus.html")