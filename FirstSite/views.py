from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')

# def uregister(request):



