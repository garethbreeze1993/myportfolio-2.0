from django.urls import path, include
from blog.views import IndexView, post_detail

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail')
]