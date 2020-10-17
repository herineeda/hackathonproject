from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.core.paginator import Paginator
from main.models import Post
from .form import NoteForm, ReNoteForm
from .models import Note, ReNote

# 쪽지함
def box(request):
    send_notes = Note.objects.filter(sender=request.user).exclude(scount=1).order_by('date') # 보낸 쪽지만
    
    # 보낸 쪽지 pagination
    send_paginator = Paginator(send_notes, 13)
    send_page = request.GET.get('page')
    send_notes = send_paginator.get_page(send_page)

    receive_notes = Note.objects.filter(receiver=request.user).exclude(rcount=1).order_by('date') # 받은 쪽지만
    # 받은 쪽지 pagination
    receive_paginator = Paginator(receive_notes, 13)
    receive_page = request.GET.get('page')
    receive_notes = receive_paginator.get_page(receive_page)
    
    send_list = list() # 사용자가 쪽지를 보낸 사람들을 담을 리스트
    receive_list = list() # 사용자에게 쪽지를 보낸 사람들을 담을 리스트

    for notes in send_notes:
        send_list.append(notes.receiver) # 사용자가 쪽지를 '보냈던' 사람들의 목록이기 때문에... 'receiver'만 가져와 리스트로 만듦.

    for notes in receive_notes:
        receive_list.append(notes.sender) # 사용자가 받은 쪽지를 보낸 사람들의 목록이기 때문에... 'sender'만 가져와 리스트로 만듦.

    send_set = set(send_list) # 중복 제거
    send_list = list(send_set) # 다시 리스트로 만들기

    recieve_set = set(receive_list)
    receive_list = list(recieve_set)

    return render(request, 'box.html', {'send_notes':send_notes, 'receive_notes':receive_notes, 'send_list':send_list, 'receive_list':receive_list})

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
    renote_form = ReNoteForm()

    if request.user != note_detail.sender: # 요청한 유저와 쪽지를 보낸 사람이 다르면...   
        note_detail.is_read = "읽음" # 해당 함수가 실행되면 is_read를 '읽음'으로 변경
        note_detail.renotes_r = 0
        note_detail.save()
    else:
        note_detail.renotes_s = 0
        note_detail.save()

    return render(request, 'note_detail.html', {'note_detail':note_detail, 'renote_form':renote_form})

# 쪽지 삭제하기
# 쪽지를 받은 사람과 보낸 사람이 모두 삭제한 경우에만 DB에서 삭제
# scount와 rcount가 0이라는 것은 삭제를 시도하지 않았다는 의미로 scount와 rcount가 모두 1인 경우에만 삭제됨.
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    # 로그인한 유저 == 보내는 사람
    if request.user == note.sender:
        note.scount = 1
        if note.rcount == 0:
            note.save()
            return redirect("box")
        note.delete()
        return redirect('box')

    # 로그인한 유저 == 받는 사람    
    else:
        note.rcount = 1
        if note.scount == 0:
            note.save()
            return redirect('box')
        note.delete()
        return redirect('box') 

# 받은 쪽지에 답장 보내기
def renote(request, note_detail_id):
    if request.method == "POST":
        renote_form = ReNoteForm(request.POST)
        ms = get_object_or_404(Note, pk=note_detail_id)
        ms.renotes_s += 1
        ms.renotes_r += 1
        ms.save()

        if renote_form.is_valid():
            temp = renote_form.save(commit=False)
            temp.author = request.user
            temp.note = Note.objects.get(pk=note_detail_id)
            temp.save()
            return redirect('note_detail',note_detail_id)