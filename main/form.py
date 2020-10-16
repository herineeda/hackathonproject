from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'name', 'category', 'content', 'image', 'url']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['title'].label = ""
        self.fields['content'].label= ""
        self.fields['image'].label =""
        self.fields['category'].label =""
        self.fields['url'].label =""

        self.fields['name'].widget.attrs.update({
            'class':'post_name',
            'placeholder': '공동구매할 제품',
        })

        self.fields['title'].widget.attrs.update({
            'class':'post_title',
            'placeholder': '게시글 제목',
        })

        self.fields['content'].widget.attrs.update({
            'class':'post_content',
            'placeholder': '내용',
        })

        self.fields['category'].widget.attrs.update({
            'class':'post_category',
        })

        self.fields['image'].widget.attrs.update({
            'class':'post_image',
        })
        self.fields['url'].widget.attrs.update({
            'class':'post_url',
            'placeholder': '제품을 판매하는 사이트 주소를 입력해주세요.',
        })

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']