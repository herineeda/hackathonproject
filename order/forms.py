from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['last_name', 'first_name', 'email', 'address', 'city', 'postal_code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "이름"
        self.fields['last_name'].label = "성"
        self.fields['email'].label= "이메일"
        self.fields['address'].label ="주소"
        self.fields['postal_code'].label ="우편번호"
        self.fields['city'].label ="상세주소"

        self.fields['first_name'].widget.attrs.update({
            'class':'first_name',
        })

        self.fields['last_name'].widget.attrs.update({
            'class':'last_name',
        })

        self.fields['email'].widget.attrs.update({
            'class':'email',
        })

        self.fields['address'].widget.attrs.update({
            'class':'address',
        })

        self.fields['postal_code'].widget.attrs.update({
            'class':'postal_code',
        })

        self.fields['city'].widget.attrs.update({
            'class':'city',
        })