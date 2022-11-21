from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
     class Meta:
         abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)
    
    
class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created_at']


class Comment(TimeStampedModel):
    owner = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    content = models.TextField(blank=False)

    class Meta:
        ordering = ['created_at']


