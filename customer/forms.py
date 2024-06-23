from django import forms

from customer.models import User


class LoginForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean_phone_number(self):
        phone_number = self.data.get('phone_number')
        if not User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Email does not exist')
        return phone_number

    def clean_password(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.data.get('password')
        try:
            user = User.objects.get(phone_number=phone_number)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Password did not match')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{phone_number} does not exist')
        return password
