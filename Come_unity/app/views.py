from django.shortcuts import redirect, render
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
    return render(request,'info.html')

def info_form(request):
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = SubscribeForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        p = form.save()
        '''
        name = form.cleaned_data['name']
        number = form.cleaned_date['phone_number']
        p = Person(name=name, phone_number=number, date_subscribed=datetime.now(), messages_recieved=0)
        p.save()
        '''
        # redirect to a new URL:
        return HttpResponseRedirect('/success/')
  # if a GET (or any other method) we'll create a blank form    
  else: 
    form = SubscribeForm()

  return render(request, 'texting/index.html', {'form': form})


