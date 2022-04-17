from django.contrib import admin
from django.urls import path
from BlogApp import views


urlpattern = [
    path('', views.PostListView,as_view(), name='post_list'),
    path('/about', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(),name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new')
]