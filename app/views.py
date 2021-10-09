from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from .models import Config, Info
import json
import os
from sawo import createTemplate, getContext, verifyToken


load = ''
loaded = 0

def setPayload(payload):
    global load
    load = payload

def setLoaded(reset=False):
    global loaded
    if reset:
        loaded=0
    else:
        loaded+=1

    
createTemplate('templates/partials')



# def index(request):
#     config = Config.objects.order_by('_api_key')[:1]
#     setLoaded()
#     setPayLoad(load if loaded<2 else '')
#     context = {"sawo":getContext(config,'main/recive') if (config) else (), "load":load, "Title":"Home"}
#     return render(request,"signin.html",context)

def index(request):
    return render(request,"index.html")

def signin(request):
    setLoaded()
    setPayload(load if loaded<2 else '')
    print(os.environ.get('api_key'))
    config = {
                "auth_key": os.environ.get('api_key'),
                "identifier": "email",
                "to": "receive"
    }
    context = {"sawo":config,"load":load,"title":"Home"}
    return render(request,'signin.html',context)

def info(request):
    if request.method=='POST':
        form=Info(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        ins=Info(name=name,email=email)
        ins.save()
        messages.success(request, 'Profile is set up Welcome to the Dashboard')
        return redirect('dashboard')
    else:
        form = Info()
    return render(request,'info.html')

def dashboard(request):
    return render(request,"dashboard.html")

def form(request):
    return render(request,"form.html")

def community(request):
    return render(request,'template.html')
