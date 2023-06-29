from django import forms
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate
from django.db.models import Q

from common.constants import DEFAULT_ERROR_MESSAGES

User = get_user_model()


class BaseForm:
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'required'


class AuthenticationForm(BaseForm, forms.Form):
    """Форма для авторизации"""

    username = forms.CharField(
        label='Логин / Номер телефона',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "0707366749",
                "autofocus": "autofocus"
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "················",
                "aria-describedby": "password"
            }
        )
    )

    def __init__(self, request=None, *args, **kwargs):
        """
        Параметр «запрос» установлен для пользовательского использования аутентификации подклассами.
        Данные формы поступают через стандартный kwarg «data».
        """
        self.username_field = None
        self.password_field = None

        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        self.username_field = self.cleaned_data.get('username')
        self.password_field = self.cleaned_data.get('password')

        if self.username_field is not None and self.password_field:
            self.user = User.objects.filter(
                Q(username=self.username_field) | Q(phone=self.username_field)
            )
            if not self.user.exists():
                self.get_invalid_login_error('invalid_email', 'email')
            elif not check_password(self.password_field, self.user.first().password):
                self.get_invalid_login_error('invalid_password', 'password')
            elif not self.user.first().is_active:
                self.get_invalid_login_error('inactive', 'email')
        return self.cleaned_data

    def get_user(self):
        return self.user.first()

    def get_invalid_login_error(self, invalid, field):
        if field == 'email':
            self._errors["email"] = DEFAULT_ERROR_MESSAGES.get(invalid)
        elif field == 'password':
            self._errors["password"] = DEFAULT_ERROR_MESSAGES.get(invalid)

        raise ValidationError(
            DEFAULT_ERROR_MESSAGES.get(invalid),
            code=invalid,
        )
