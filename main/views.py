from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post

# 서비스 소개 페이지
def introduce(request):
    return render(request, 'introduce.html')

# 공구 게시판: 게시글 목록 띄우기
def group_purchase(request):
    posts = Post.objects.all()
    return render(request, 'grouppurchase.html',{'posts':posts})

# 게시글 자세히 보기
def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post_detail':post_detail})

# 게시글 작성 페이지
def new(request):
    return render(request, 'create.html')

# 게시글 작성
def create(request):
    post = Post()
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.image = request.FILES['images']
    post.date = timezone.datetime.now()
    post.author = User.objects.get(username = request.user.get_username())
    post.save()
    return redirect('/main/post_detail/' + str(post.id))

    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.date = timezone.now()
    #         post.author = User.objects.get(username = request.user.get_username())
    #         post.save()
    #         return redirect('group_purchase')
    # else:
    #     form = PostForm()
    #     return render(request, 'create.html', {'form':form}