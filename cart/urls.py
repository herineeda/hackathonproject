from django.urls import path

from .views import *

app_name = 'cart'

urlpatterns = [

    path('detail/', detail, name='detail'),

    # 장바구니에 상품 추가하는 페이지로 이동하는 경로
    path('add/<int:product_id>/', add, name='product_add'),

    # 장바구니에서 물품 수량 변경
    path('update/<int:product_id>/', update, name='product_update'),

    # 장바구니에서 상품 삭제하는 view로 이동하는 경로
    path('remove/<int:product_id>/', remove, name='product_remove'),

]
