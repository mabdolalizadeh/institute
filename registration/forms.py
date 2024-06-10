from django import forms

from registration.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'phone_number', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'اسمتون...'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'شماره‌تون...'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمزتون...'}),
        }
        labels = {
            'full_name': '',
            'phone_number': '',
            'password': '',
        }
