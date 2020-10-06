from django.urls import path
from . import views

urlpatterns = [
    path('notebox/', views.box, name="box"), # 쪽지함
    path('notebox/note/<int:note_id>', views.note_detail, name='note_detail'), # 쪽지 자세히 보기
    path('post/<int:post_id>/send_note/<str:receiver>', views.create_note, name="create_note"), # 쪽지 보내기
    path('notebox/note/<int:note_id>/delete', views.note_delete, name="note_delete"), # 쪽지 삭제하기
]