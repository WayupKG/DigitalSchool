import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from common import constants as const
from common.upload_to_file import user_avatar


class User(AbstractUser):
    """"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    GENDER: tuple[tuple[str]] = (
        (const.MEN, 'Мужчина'),
        (const.WOMEN, 'Женщина'),
    )
    USER_TYPE: tuple[tuple[str]] = (
        (const.ADMIN, 'Администратор'),
        (const.TEACHER, 'Учитель'),
        (const.STUDENT, 'Ученик'),
    )
    phone = models.CharField('Номер телефона', max_length=255, unique=True)
    date_birth = models.DateField('Дата рождение', null=True)
    gender = models.CharField('Пол', max_length=10, choices=GENDER, default=const.MEN)
    user_type = models.CharField(choices=USER_TYPE, max_length=20, default=const.ADMIN, editable=False)
    avatar = ProcessedImageField(verbose_name='Обложка', upload_to=user_avatar,
                                 format='webp', processors=[ResizeToFill(500, 500)],
                                 options={'quality': 90}, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self) -> str:
        return str(self.get_full_name())

    def get_gender(self):
        return dict(self.GENDER)[self.gender]


class Teacher(User):
    """ Учитель """
    subject = models.CharField('Название предмета', max_length=100)

    def save(self, *args, **kwargs):
        self.user_type = const.TEACHER
        super().save(**kwargs)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учители'


class Student(User):
    """ Ученик """
    address = models.CharField('Адрес', max_length=255)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def save(self, *args, **kwargs):
        self.user_type = const.STUDENT
        super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('students_detail', kwargs={'uuid': str(self.id)})

    def get_update_url(self):
        return reverse('students_update', kwargs={'uuid': str(self.id)})

    def get_delete_url(self):
        return reverse('students_delete', kwargs={'uuid': str(self.id)})
