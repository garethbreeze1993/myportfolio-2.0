from django.urls import path, include
from blog.views import IndexView, post_detail, contact_view

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('contact/', contact_view, name='contact')
]