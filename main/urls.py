from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('introduce/', views.introduce, name="introduce"), # 서비스 소개
    path('group_purchase/', views.group_purchase, name="group_purchase"), # 공동구매 게시판
    path('post/<int:post_id>', views.post_detail, name="post_detail"), # 게시글 자세히 보기
    path('create/', views.create, name="create"), # 글 작성하기
    path('search/', views.search, name="search"), # 글 검색하기    
    path('post/<int:post_id>/edit/', views.edit, name="edit"), # 글 수정하기
    path('post/<int:post_id>/delete/', views.delete, name="delete"), # 글 삭제하기
    path('post/<int:post_id>/comment', views.comment, name="comment"), # 댓글 작성하기
    path('post/<int:post_id>/comment<int:comment_id>/delete', views.comment_delete, name="comment_delete"), # 댓글 삭제하기
    path('mypage', views.mypage, name="mypage"), # 마이페이지
    path('mypage/post_closed/<int:post_id>', views.closed, name="closed"), # 공구 성공 표시
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)