from django import forms

from registration.models import Profile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'یه رمز خوب انتخاب کنید...',
                                                                'class': 'input100'}), label='')

    class Meta:
        model = Profile
        fields = ['full_name', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'اسمتون...',
                                                'class': 'input100'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'شماره‌تون...',
                                                     'class': 'input100'}),
        }
        labels = {
            'full_name': '',
            'phone_number': '',
        }

        errors = {
            'full_name': {
                'required': 'اسمتو حتما باید پر کنی',
                'invalid': 'اسمتو اشتباه نوشتی',
            }
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 11 or len(phone_number) > 12:
            self.add_error('phone_number', 'شماره‌تونو اشتباه وارد کردید...')
        return phone_number


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمزتون...',
                                                                 'class': 'input100'}), label='')

    class Meta:
        model = Profile
        fields = ['phone_number', ]
        widgets = {
            'phone_number': forms.NumberInput(attrs={'placeholder': 'شماره‌تون...',
                                                     'class': 'input100'}),
        }
        labels = {
            'phone_number': '',
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 11 or len(phone_number) > 12:
            self.add_error('phone_number', 'شماره‌تونو اشتباه وارد کردید...')

        return phone_number