from os import lseek
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView)
from BlogApp.models import Post, Comment
from BlogApp.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timezone
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'
    ##test for commit file
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).orber_by('-published_date'))

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class DraftPostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).orber_by('-published_date'))
