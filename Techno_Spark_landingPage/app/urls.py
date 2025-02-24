# user_registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HOME, name="home"),
    path('register', views.lead_registration, name="register")
]
