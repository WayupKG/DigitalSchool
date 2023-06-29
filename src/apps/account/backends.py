from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend

from apps.account.models import Teacher, Student

User = get_user_model()


class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(
                Q(username=username) | Q(phone=username)
            )
        except User.DoesNotExist:
            return None
        return user if user.check_password(password) else None