
from django.shortcuts import render, redirect 
from django.shortcuts import Post

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import generic
# from django.views.generic.list import ListView


class PostListView(generic.ListView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


class PostCreateView(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


class PostDetailView(generic.DetailView): 
    model = Post   
    fields = '__all__'  
    success_url  = reverse_lazy('blog:all')


class  PostUpdateView(generic.UpdateView):
    model = Post 
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


class  PostDeleteView(generic.UpdateView):
    model = Post  
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
