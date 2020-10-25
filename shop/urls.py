from django.urls import path

from .views import *

app_name = 'shop'
urlpatterns = [
    path('product/', product_in_category, name='product_all'),
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
    path('<int:id>/<product_slug>/<str:category>/review', review, name='review'), # 리뷰 작성하기
    path('<int:id>/<product_slug>/<str:category>/review<int:review_id>/delete', delete_review, name='delete_review'), # 리뷰 삭제하기
]