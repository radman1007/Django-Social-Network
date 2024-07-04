from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'social'

urlpatterns = [
    path('login/', views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', views.log_out, name="logout"),
]
