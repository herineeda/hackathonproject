from django.shortcuts import render

# 서비스 소개 페이지
def introduce(request):
    return render(request, 'introduce.html')

