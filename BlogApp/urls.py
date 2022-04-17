from django.contrib import admin
from django.urls import path


urlpattern = [
    path('/about', views.AboutView.as_view(), name='about')
]