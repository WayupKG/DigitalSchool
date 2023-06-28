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

    def __init__(self):
        self.model_list = [User, Teacher, Student]
        super().__init__()

    def get_user(self, user_id):
        user = self.down_cast_user_type(user_id, 'user_id')
        return user if user else None

    def authenticate(self, request, username, password):
        user = self.down_cast_user_type(username)
        if user:
            return user if user.check_password(password) else None
        return None

    def down_cast_user_type(self, username: str, field='username'):
        for model in self.model_list:
            if field == 'username':
                user = model.objects.filter(phone=username)
            else:
                user = model.objects.filter(id=username)
            if user.exists():
                return user.first()
        return None
