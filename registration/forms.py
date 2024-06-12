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

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 11 or len(phone_number) > 12:
            self.add_error('phone_number', 'شماره‌تونو اشتباه وارد کردید...')
