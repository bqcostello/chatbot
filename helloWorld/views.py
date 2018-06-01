from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h2>Dear Dr. Siy, I was so excited to get this working that I had to tell my boyfriend. So I am editing the 'Hello World' text a little.\n I LOVE YOU CALEB JOSEPH MICHAEL LEWIS PETERSEN!</h2>")

# Create your views here.
