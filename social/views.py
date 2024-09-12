from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def log_out(request):
    logout(request)
    return HttpResponse("home") 


def profile(request):
    return HttpResponse("home")