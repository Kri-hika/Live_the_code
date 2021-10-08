from django.shortcuts import render
from django.http import HttpResponse
from .models import Config 
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

def receive(request):
    if request.method == 'POST':
        payload = json.loads(request.body)["payload"]
        setLoaded(True)
        setPayload(payload)
        print(payload)
        
        status = 200 if verifyToken(payload) else 404
        print(status)
        response_data = {"status":status}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

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

def signup(request):
    return render(request,'signup.html')