from django.db import models


class School(models.Model):
    """Школа"""
    title = models.CharField('Название', max_length=255)
    classrooms = models.ManyToManyField(
        'ClassRoom',
        through='RelationshipSchoolClassRoom',
        related_name='school'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self) -> str:
        return str(self.title)


class ClassRoom(models.Model):
    """Класс"""
    title = models.CharField('Название', max_length=255)
    teacher = models.ForeignKey(
        'account.Teacher',
        verbose_name='Учитель',
        on_delete=models.PROTECT,
        related_name='classrooms'
    )
    students = models.ManyToManyField(
        'account.Student',
        verbose_name='Ученики',
        through='RelationshipClassRoomStudent',
        related_name='classroom'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self) -> str:
        return str(self.title)


class RelationshipSchoolClassRoom(models.Model):
    """Отношения между школой и классом"""
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classroom = models.OneToOneField(ClassRoom, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.school} - {self.classroom}"


class RelationshipClassRoomStudent(models.Model):
    """Отношения между классом и учеником"""
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    student = models.OneToOneField('account.Student', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.classroom} - {self.student}"
