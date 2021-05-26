from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.image_name} for the post {self.post}'

