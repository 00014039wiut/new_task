from django import forms

from customer.models import User, Customer


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


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'password']

    def clean_phone_number(self):
        phone_number = self.data.get('phone_number').lower()
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(f'The {phone_number} is already registered')
        return phone_number

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password didn\'t match')
        return password


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone_number', 'email', 'address', 'image']


class EmailForm(forms.Form):
    subject = forms.CharField(label='Subject', widget=forms.TextInput())
    message = forms.CharField(label='Message', widget=forms.Textarea())
    from_email = forms.EmailField(label='From', widget=forms.TextInput())
    to_email = forms.EmailField(label='To', widget=forms.TextInput())
