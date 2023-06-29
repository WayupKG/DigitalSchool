from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from workers.send_mail import send_mail_registration


@receiver(post_save, sender=Student)
def send_registration_notification_mail(sender, instance, created, *args, **kwargs):
    if created:
        user_data = {
            'full_name': instance.get_full_name(),
            'email': instance.email,
        }
        send_mail_registration(user_data)
