from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserModel
from django.core.exceptions import ValidationError
from django.utils.text import capfirst


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    phone_number/password logins.
    """

    phone_number = forms.Textarea()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": (
            "Please enter a correct %(phone_number)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": ("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "phone_number" field.
        self.phone_number_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        phone_number_max_length = self.phone_number_field.max_length or 254
        self.fields["phone_number"].max_length = phone_number_max_length
        self.fields["phone_number"].widget.attrs["maxlength"] = phone_number_max_length
        if self.fields["phone_number"].label is None:
            self.fields["phone_number"].label = capfirst(self.phone_number_field.verbose_name)

    def clean(self):
        phone_number = self.cleaned_data.get("phone_number")
        password = self.cleaned_data.get("password")

        if phone_number is not None and password:
            self.user_cache = authenticate(
                self.request, phone_number=phone_number, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"phone_number": self.phone_number_field.verbose_name},
        )
