from os import lseek
from django.shortcuts import redirect, render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from BlogApp.models import Post, Comment
from BlogApp.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import timezone
from django.urls import reverse_lazy
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'
    ##test for git alias
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

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
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')