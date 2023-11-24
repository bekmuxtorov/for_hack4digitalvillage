from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/login/', views.UserLoginApiView.as_view(), name='login_view'),
    path('auth/register/', views.AccountRegisterAPIView.as_view(),
         name='register_view'),

]
