from django.shortcuts import render
from django.http import HttpResponse
from .models import Workspace

# Create your views here.
def workspace_hello(request):
    return HttpResponse('Hey there! This is your work-space :))')