from django.db import models
from user.models import Users


class Post(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    content = models.CharField(max_length=500, blank=False)
    views = models.IntegerField(default=0)
