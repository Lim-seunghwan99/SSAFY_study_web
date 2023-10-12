from django.db import models
from django.conf import settings
# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
from accounts.models import User
# user = models.ForeignKey(User, on_delete=models.CASCADE)
from django.contrib.auth import get_user_model
# user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
