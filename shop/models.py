from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='category', blank=True)

    class meta:
        ordering = ['name']
        verbose_name = 'category' 
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, related_name='products') #카테고리가 지워져도 제품은 살리게
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='product', blank=True)
    description = models.TextField(blank=True) #상세페이지에 설명 되어있는것 
    meta_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2) 
    stock = models.PositiveIntegerField()
    available_display = models.BooleanField('Display', default=True) 
    available_order = models.BooleanField('order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 리뷰의 개수
    count = models.IntegerField(default=0)


    class Meta: 
        ordering = ['-created', '-updated']
        index_together = [['id','slug']]
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])
    
    def summary(self):
        return self.description[:100]

# 상품 리뷰
class Review(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    rate = models.IntegerField(default=1)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.content[:20]