from django.db import models
from django.contrib.auth.models import User
from main.models import Post

class Note(models.Model):
    sender = models.ForeignKey(User, default="알 수 없음", on_delete=models.SET_DEFAULT)
    receiver = models.CharField(max_length=100)
    date = models.DateTimeField()
    is_read = models.CharField(max_length=10, default="읽지 않음")
    content = models.TextField()
    scount = models.IntegerField(default=0)
    rcount = models.IntegerField(default=0)
    post = models.ForeignKey(Post, default="존재하지 않는 글", on_delete=models.SET_DEFAULT)
    renotes_s = models.IntegerField(default=0)
    renotes_r = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:10]

    def summary(self):
        return self.content[:20]

class ReNote(models.Model):
    author = models.ForeignKey(User, default="알 수 없음", on_delete=models.SET_DEFAULT)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

