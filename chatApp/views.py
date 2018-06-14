from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hey there! What is it that you've done today?")

def results(request):
    response = "Results: " 
    return HttpResponse(response)
