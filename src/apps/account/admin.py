from django.contrib import admin, auth
from django.contrib.auth.hashers import check_password, make_password

from .models import Student, Teacher

User = auth.get_user_model()


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """ Пользователь """
    list_display = (
        'email',
        'get_full_name',
        'is_superuser',
        'is_active',
        'is_staff',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_superuser',
        'is_active',
        'is_staff'
    )
    search_fields = ['get_full_name', 'email']
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        if obj.pk:
            user_database = User.objects.get(pk=obj.pk)
            if not (check_password(form.data['password'], user_database.password) or user_database.password ==
                    form.data['password']):
                obj.password = make_password(obj.password)
            else:
                obj.password = user_database.password
        else:
            # New user
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    """ Пользователь """


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    """ Пользователь """
