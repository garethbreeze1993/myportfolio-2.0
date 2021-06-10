from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Image


class IndexView(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'post_list'
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-last_modified')


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = post.images.all()
    return render(request, 'blog/detail.html', context={'post_obj': post, 'images': images})

'''
Pagination

https://docs.djangoproject.com/en/3.2/topics/pagination/
'''