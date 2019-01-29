from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

def home(request):
	return render(request, 'home.html', context={}, ) #context is empty unless we want to incorporate data into our landing page

def live(request):
    return render(request, 'live.html', context={}, )