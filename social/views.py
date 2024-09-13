from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def log_out(request):
    logout(request)
    return HttpResponse("home") 

def profile(request):
    return HttpResponse("home")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Account.object.create(user=user)
            return render(request, 'registration/register_done.html', {'user' : user})
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form' : form}) 