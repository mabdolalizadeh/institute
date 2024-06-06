from django import forms
from .models import SimpleSignup


class SimpleSignupModelForm(forms.ModelForm):
    class Meta:
        model = SimpleSignup
        fields = ['name', 'email', 'phone', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'اسمتون...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل‌تون...'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'شماره‌تون...'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'یه کم توضیح میدی راجع به اینکه قبلا زبان کار کردی یا نه؟...'}),
        }
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'text': '',
        }
        error_messages = {
            'name': {
                'required': 'این مهمه. حتما پرش کن',
                'invalid': 'تو نوشتن اسمت یه اشتباهی کردی یه چک بکن'
            },
            'email': {
                'required': 'این مهمه. حتما پرش کن',
                'invalid': 'تو نوشتن ایمیلت یه اشتباهی کردی یه چک بکن'
            },
            'phone': {
                'required': 'این مهمه. حتما پرش کن',
                'invalid': 'تو نوشتن شماره‌ت یه اشتباهی کردی یه چک بکن'
            },
            'text': {
                'required': 'این مهمه. حتما پرش کن',
                'invalid': 'تو نوشتن متنت یه اشتباهی کردی یه چک بکن'
            }
        }
