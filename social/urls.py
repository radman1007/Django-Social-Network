from django.urls import path
from . import views 
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'social'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', views.log_out, name="logout"),
]
