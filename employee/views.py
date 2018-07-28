from django.shortcuts import render
from .import views
from django.http import HttpResponse 
import json



# Create your views here.

def practice(request):
	return HttpResponse("hi")

