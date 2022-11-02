from django.shortcuts import render
from django.shortcuts import render
from app.models import *


# Create your views here.
def display_topic(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    W=Webpage.objects.all()
    d={'webpages':W}
    return render(request,'display_webpage.html',d)

def display_accessrecords(request):
    a=accessrecords.objects.all()
    d={'accessrecords':a}
    return render(request,'display_accessrecords.html',d)
