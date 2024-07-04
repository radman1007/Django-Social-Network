from django.shortcuts import render, redirect

def log_out(request):
    logout(request)
    return redirect(request.Meta.get('HTTP_REFERER'))