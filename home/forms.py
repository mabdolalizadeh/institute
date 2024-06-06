from django import forms
from .models import SignupInHome


class SignupInHomeModelForm(forms.ModelForm):
    class Meta:
        model = SignupInHome
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
