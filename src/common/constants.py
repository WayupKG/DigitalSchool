from django.utils.translation import gettext_lazy as _

MEN: str = 'men'
WOMEN: str = 'women'
STUDENT: str = 'student'
TEACHER: str = 'teacher'

DEFAULT_ERROR_MESSAGES = {
    'invalid_email': _("Пользователь с такой электронной почтой не существует."),
    'invalid_password': _('Пожалуйста, введите правильный пароль. Обратите внимание, что пароль чувствителен к регистру.'),
    'inactive': _("Ваша учетная запись находится на рассмотрении."),
    'invalid_password_confirm': _("Пароли не совпадают"),
    'invalid_activated_code': _('Недействительный код активации.'),
    'invalid_activated_code_not_digit': _('Код активации должен содержать только цифры.'),
    'no_activated_code': _('Не правильный код активации.'),
    'invalid_uuid': _('Ссылка недействительно, ссылка было повреждено или изменено.'),
    'invalid_old_password': _('Ваш старый пароль был введен неправильно. Пожалуйста, введите его снова.')
}
