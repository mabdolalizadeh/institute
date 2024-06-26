from django import forms

from registration.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'اسمتون...',
                                                'class': 'input100'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'شماره‌تون...',
                                                     'class': 'input100'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'یه رمز خوب انتخاب کنید...',
                                                   'class': 'input100'}),
        }
        labels = {
            'full_name': '',
            'phone_number': '',
            'password': '',
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
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        widgets = {
            'phone_number': forms.NumberInput(attrs={'placeholder': 'شماره‌تون...',
                                                     'class': 'input100'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمزتون...',
                                                   'class': 'input100'})
        }
        labels = {
            'phone_number': '',
            'password': ''
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 11 or len(phone_number) > 12:
            self.add_error('phone_number', 'شماره‌تونو اشتباه وارد کردید...')

        return phone_number

    def clean_password(self):
        phone_number = self.cleaned_data['phone_number']
        password = self.cleaned_data['password']

        if not User.objects.filter(phone_number__iexact=phone_number,
                                   password__iexact=password).exists():
            self.add_error('password', 'رمز اشتباهه')

        return password
