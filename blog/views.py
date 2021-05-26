from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Image


class IndexView(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'post_list'
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-last_modified')

