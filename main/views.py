from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Post
from .form import PostForm
from django.db.models import Q

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
    # post_detail.count += 1 
    return render(request, 'post_detail.html', {'post_detail':post_detail})

# 게시글 작성 페이지
def new(request):
    return render(request, 'create.html')

# 게시글 작성
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.datetime.now()
            post.author = User.objects.get(username = request.user.get_username())
            post.success = False
            post.save()
            return redirect('group_purchase')
    else:
        form = PostForm()
        return render(request, 'create.html', {'form':form})

    # post = Post()
    # post.title = request.POST['title']
    # post.name = request.POST['name']
    # post.content = request.POST['content']
    # post.image = request.FILES['images']
    # post.category = request.POST['category']
    # post.deadline = request.POST['deadline']
    # post.url = request.POST['url']
    # post.date = timezone.datetime.now()
    # post.author = User.objects.get(username = request.user.get_username())
    # post.save()
    # return redirect('/main/post/' + str(post.id))

# 게시글 수정, 장고 폼 이용 시 코드 수정하기
def edit(request, post_detail_id):
    post = get_object_or_404(Post, pk=post_detail_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('group_purchase')
    else:
        form = PostForm(instance=post)
        return render(request, 'create.html', {'form':form})

    # post = get_object_or_404(Post, pk=post_detail_id)

    # if request.method == "POST":
    #     post.title = request.POST['title']
    #     post.name = request.POST['name']
    #     post.content = request.POST['content']
    #     post.image = request.FILES['images']
    #     post.category = request.POST['category']
    #     post.deadline = request.POST['deadline']
    #     post.url = request.POST['url']
    #     post.author = User.objects.get(username = request.user.get_username())
    #     post.save()
    #     return redirect('/main/post/' + str(post.id))

    # return render(request, 'edit.html', {'post':post})

# 게시글 삭제, 임시로 삭제 후 글 전체 목록 띄우기
def delete(request, post_detail_id):
    post = get_object_or_404(Post, pk=post_detail_id)
    post.delete()
    return redirect('group_purchase')

# 공동구매 글 검색하기
def search(request):
    choice = request.GET.get('select_text')
    keyword = request.GET.get('text')

    if choice == "전체":
        result = Post.objects.filter(Q(name__contains=keyword) | Q(content__contains=keyword))
    elif choice == "제품명":
        result = Post.objects.filter(name__contains=keyword)
    else:
        result = Post.objects.filter(content__contains=keyword)
    return render(request, 'grouppurchase.html', {'posts':result})

