from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ""
        self.fields['content'].label = ""

        self.fields['title'].widget.attrs.update({
            'class':'note_title',
            'placeholder':'쪽지 제목을 적어주세요',
        })

        self.fields['content'].widget.attrs.update({
            'class':'note_content',
            'placeholder':'쪽지 내용을 적어주세요',
        })