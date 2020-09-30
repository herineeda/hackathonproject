from django.db import models
from django.contrib.auth.models import User
from shop.models import Category

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title