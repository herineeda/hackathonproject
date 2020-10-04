from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'title', 'content', 'image', 'category', 'url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "제품명"
        self.fields['title'].label = "제목"
        self.fields['content'].label= "내용"
        self.fields['category'].label ="분류"

        self.fields['name'].widget.attrs.update({
            'class':'post_name',
            'placeholder': '공동구매할 제품명을 입력하세요.',
        })

        self.fields['title'].widget.attrs.update({
            'class':'post_title',
        })

        self.fields['content'].widget.attrs.update({
            'class':'post_content',
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
        fields = ['secret', 'content']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['secret'].label = "비밀댓글"
            self.fields['content'].label = " "

            self.fields['secret'].widget.attrs.update({
                'class':'comment_secret',
            })

            self.fields['content'].widget.attrs.update({
                'class': 'comment_content',
            })