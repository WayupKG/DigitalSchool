from django.apps import AppConfig
from django.core.signals import request_finished


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.account'

    def ready(self):
        import apps.account.signals
