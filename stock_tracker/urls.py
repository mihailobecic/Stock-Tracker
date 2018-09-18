"""Stox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='Stox-Home'),
    path('Portfolio/<int:pk>', views.PortfolioView.as_view(), name='Portfolio'),
    path('Portfolio/new/', views.PortfolioCreate.as_view(), name='Portfolio-create'),
    path('Portfolio/<int:pk/AddStock>', views.AddStock.as_view(), name='AddStock'),
]
