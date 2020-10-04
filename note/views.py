from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from main.models import Post
from .models import Note
from .form import NoteForm

# 쪽지함
def box(request):
    send_notes = Note.objects.filter(sender=request.user).exclude(scount=1)
    receive_notes = Note.objects.filter(receiver=request.user).exclude(rcount=1)
    return render(request, 'box.html', {'send_notes':send_notes, 'receive_notes':receive_notes})

# 쪽지 작성
def create_note(request, post_id, receiver):
    if request.method == "POST":
        note = NoteForm(request.POST)

        if note.is_valid():
            temp = note.save(commit=False)
            temp.sender = request.user
            temp.receiver = receiver
            temp.date = timezone.datetime.now()
            temp.is_read = "읽지 않음"
            temp.post = get_object_or_404(Post, pk=post_id)
            temp.save()
            return redirect('post_detail', post_id)

    note_form = NoteForm
    return render(request, 'note.html', {'note_form':note_form})

# 쪽지 자세히 보기
def note_detail(request, note_id):
    note_detail = get_object_or_404(Note, pk=note_id)

    if request.user != note_detail.sender: # 요청한 유저와 쪽지를 보낸 사람이 다르면...   
        note_detail.is_read = "읽음" # 해당 함수가 실행되면 is_read를 True로 변경
        note_detail.save()

    return render(request, 'note_detail.html', {'note_detail':note_detail})

# # 쪽지 삭제하기
# # 쪽지를 받은 사람과 보낸 사람이 모두 삭제한 경우에만 DB에서 삭제
# # scount와 rcount가 0이라는 것은 삭제를 시도하지 않았다는 의미로 scount와 rcount가 모두 1인 경우에만 삭제됨.
# def delete_note(request, note_detail_id):
#     note = get_object_or_404(Note, pk=note_detail_id)

#     # 로그인한 유저 == 보내는 사람
#     if request.user == note.sender:
#         if note.scount == 0:
#             note.scount = 1
#             if note.rcount == 0:
#                 note.save()
#                 return redirect("box")
#             note.delete()
#             return redirect('box')

#     # 로그인한 유저 == 받는 사람    
#     else:
#         if note.rcount == 0:
#             note.rcount = 1
#             if note.scount == 0:
#                 note.save()
#                 return redirect('received_notes')
#             note.delete()
#             return redirect('received_notes')    

# # 상대방이 쪽지를 읽지 않은 경우, 쪽지를 수정
# def update(request, note_detail_id):
#     note = Note.objects.get(pk=note_detail_id)
#     update_form = NoteForm(instance=note) # 수정할 글 담아오기!!

#     if not note.is_read:
#         if request.method == 'POST':
#             update_form = NoteForm(request.POST, instance=note) # instance가 빠지면 새로운 글이 생성됨.

#             if update_form.is_valid():
#                 update_form.save(commit=False)
#                 update_form.send_at = timezone.datetime.now()
#                 update_form.save()
#                 return redirect('detail', note_detail_id)
#     else:
#         pass # 경고창 띄우는 법 생각해보기.. 지금은 모르겠다.
#     return render(request, 'message.html', {'note_form':update_form})