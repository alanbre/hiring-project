from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'new_home.html')

def dashboard(request):
    return render(request, 'dashboard.html')