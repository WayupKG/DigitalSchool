from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from common import constants as const
from common.upload_to_file import user_avatar


class User(AbstractUser):
    """"""
    GENDER: tuple[tuple[str]] = (
        (const.MEN, 'Мужчина'),
        (const.WOMEN, 'Женщина'),
    )
    phone = models.CharField('Номер телефона', max_length=255, unique=True)
    gender = models.CharField('Пол', max_length=10, choices=GENDER, default=const.MEN)
    avatar = ProcessedImageField(verbose_name='Обложка', upload_to=user_avatar,
                                 format='webp', processors=[ResizeToFill(500, 500)],
                                 options={'quality': 90}, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self) -> str:
        return str(self.get_full_name())


class Teacher(User):
    """ Учитель """
    subject = models.CharField('Название предмета', max_length=100)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учители'


class Student(User):
    """ Ученик """
    address = models.CharField('Адрес', max_length=255)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
