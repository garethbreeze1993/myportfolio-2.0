from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Post, Image
from blog.forms import ContactForm
from myportfolio.settings import DEFAULT_FROM_EMAIL



class IndexView(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'post_list'
    paginate_by = 6
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-last_modified')


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = post.images.all()
    return render(request, 'blog/detail.html', context={'post_obj': post, 'images': images})


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['default@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # TODO Implement flash messages
            return redirect('home')
    return render(request, "blog/email.html", {'form': form})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')


'''
https://learndjango.com/tutorials/django-email-contact-form
'''