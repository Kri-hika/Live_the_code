from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')