from django.contrib import admin
from django.urls import path


urlpattern = [
    path('', views.PostListView,as_view(), name='post_list'),
    path('/about', views.AboutView.as_view(), name='about')
]