from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # 상품을 분류할 카테고리들, 필요하면 추가하기
    drink = '음료'
    food = '음식'
    household_item = '생활용품'
    etc = '기타'
    category_choices = ((drink, '음료'),(food, '음식'), (household_item, '생활용품'), (etc, '기타'))

    title = models.CharField(max_length=200, null=False)
    date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)

    # 공구할 제품  정보
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=category_choices, default='기타')
    # deadline = models.DateTimeField('date published', default='2020-10-01 10:10')
    # url = models.URLField("group purchase product url", default='https://www.google.co.kr/')

    success = models.BooleanField(default=False) # 공구가 성공했는지...
    url = models.URLField("출처")
    count = models.IntegerField(default=0) # 조회수

    #조회수
    #count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

        def summary(self):
            return self.content[:100]

# 게시글에 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=300)
    date = models.DateTimeField()
    secret = models.BooleanField(default=False) # 비밀 댓글 여부

    def __str__(self):
        
        return self.content 