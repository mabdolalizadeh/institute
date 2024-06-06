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
