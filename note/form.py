from django import forms

from .models import Note, ReNote


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ""

        self.fields['content'].widget.attrs.update({
            'class':'create_note',
            'placeholder':'쪽지 내용을 적어주세요',
        })

class ReNoteForm(forms.ModelForm):

    class Meta:
        model = ReNote
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label =""
        
        self.fields['content'].widget.attrs.update({
            'class':'re_note_form',
            'rows':3, 
        })