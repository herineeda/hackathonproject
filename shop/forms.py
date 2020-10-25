from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = ""
        self.fields['content'].label = ""

        self.fields['image'].widget.attrs.update({
            'class':'review_image',
        })

        self.fields['content'].widget.attrs.update({
            'class':'review_content',
            'placeholder': '리뷰를 작성해주세요',
        })