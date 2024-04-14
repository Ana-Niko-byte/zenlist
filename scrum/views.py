from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def scrum_hello(response):
    return HttpResponse('Hello from the Scrum Home page!')