from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.conf import settings

from config.celery import app

User = get_user_model()


@app.task
def send_mail_registration(user_data):
    title, from_email = settings.EMAIL_TITLE_FROM, settings.EMAIL_HOST_USER
    title_send = 'Регистрация на сайте "El-School"'
    to_form, headers = f'{user_data.get("full_name")} <{user_data.get("email")}>', {'From': f'{title} <{from_email}>'}
    html_content = render_to_string('send_mail/registration.html', user_data)
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(title_send, text_content, from_email, [to_form], headers=headers)
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)
    return str(f'Sent to {user_data.get("email")}')
