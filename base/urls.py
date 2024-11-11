# base/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),

]
