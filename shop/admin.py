from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug': ['name',]} #카테고리 자동으로 동작하게 할거다 튜플형태로 등록 

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','price','stock','available_display','available_order','created','updated']
    list_filter = ['available_display','created','updated','category']
    list_editable = ['price', 'stock','available_display','available_order'] 
    prepopulated_fields = {'slug':['name',]}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)