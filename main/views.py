from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .form import CommentForm, PostForm
from .models import Comment, Post


# 서비스 소개 페이지
def introduce(request):
    return render(request, 'introduce.html')


# 공구 게시판: 게시글 목록 띄우기
def group_purchase(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 13)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'grouppurchase.html', {'posts': posts})


# 게시글 자세히 보기
def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    post_detail.count += 1
    post_detail.save()
    comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post_detail': post_detail, 'comment_form': comment_form})


# 게시글 작성
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.datetime.now()
            post.author = User.objects.get(
                username=request.user.get_username())
            post.success = False
            post.save()
            return redirect('group_purchase')
    else:
        form = PostForm()
        return render(request, 'create.html', {'form': form})


# 게시글 수정
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('mypage')

    else:
        form = PostForm(instance=post)
        return render(request, 'create.html', {'form': form})


# 게시글 삭제
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('mypage')


# 공동구매 글 검색하기
def search(request):
    choice = request.GET.get('select_text')
    keyword = request.GET.get('text')

    if choice == "전체":
        result = Post.objects.filter(
            Q(name__contains=keyword) | Q(content__contains=keyword))
    elif choice == "제품명":
        result = Post.objects.filter(name__contains=keyword)
    else:
        result = Post.objects.filter(content__contains=keyword)

    paginator = Paginator(result, 13)
    page = request.GET.get('page')
    result = paginator.get_page(page)

    return render(request, 'grouppurchase.html', {'posts': result})


# 마이페이지
def mypage(request):
    # 내가 작성한 글만 가져오기
    user = User.objects.get(username=request.user.get_username())
    mypost_list = Post.objects.filter(author=user)

    # 내가 작성한 글 pagination
    mypost_paginator = Paginator(mypost_list, 6)
    post_page = request.GET.get('page')
    myposts = mypost_paginator.get_page(post_page)

    # 댓글을 단 글만 가져오기
    mycomments = Comment.objects.filter(writer=user)  # 작성한 댓글 가져오기

    # Comment 객체에서 Post 객체를 가져와 리스트에 담기(Comment 모델이 Post 모델을 외래키로 참조!!)
    comment_posts_list = list()
    for mycomment in mycomments:
        comment_posts_list.append(mycomment.post)

    # 중복 제거(한 글에 여러 댓글을 작성했을 수도 있으니까!)
    comment_post_set = set(comment_posts_list)
    comment_posts_list = list(comment_post_set)

    # 댓글 단 글 pagination
    comment_paginator = Paginator(comment_posts_list, 6)
    comment_page = request.GET.get('page')
    comment_posts = comment_paginator.get_page(comment_page)

    return render(request, 'mypage.html', {'myposts': myposts, 'comment_posts': comment_posts})


# 공구 종료시키는 버튼
def closed(request, post_id):
    closed_post = get_object_or_404(Post, pk=post_id)
    closed_post.success = True
    closed_post.save()
    return redirect('mypage')


# 게시글에 댓글 달기
def comment(request, post_id):
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        temp = comment_form.save(commit=False)
        temp.post = Post.objects.get(pk=post_id)
        temp.writer = request.user
        temp.date = timezone.datetime.now()
        temp.save()
        return redirect('post_detail', post_id)


# 댓글 삭제
def comment_delete(request, post_id, comment_id):
    my_comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == my_comment.writer:
        my_comment.delete()
        return redirect('post_detail', post_id)

    else:
        raise PermissionDenied


# SSL 인증서 적용
def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)
