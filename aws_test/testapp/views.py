from django.shortcuts import render
from django.http import *

# Create your views here.



def test_view(request,name):
    data = "Hi, Welcome {}, this is first view in AWS....".format(name)
    return HttpResponse(data)