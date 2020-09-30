from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('introduce/', views.introduce, name="introduce"), # 서비스 소개
    path('group_purchase/', views.group_purchase, name="group_purchase"), # 공동구매 게시판
    path('post_detail/<int:post_id>', views.post_detail, name="post_detail"), # 게시글 자세히 보기
    path('new/', views.new, name="new"), # 폼 띄우기
    path('create/', views.create, name="create"), # 글 작성하기
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)