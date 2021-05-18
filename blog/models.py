from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

# class Images(models.Model):
#     note = models.ForeignKey(Post,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=user_directory_path,null=True,blank=True)