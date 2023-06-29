from django.contrib import admin

from .models import School, ClassRoom, RelationshipSchoolClassRoom, RelationshipClassRoomStudent


class RelationshipSchoolClassRoomInline(admin.TabularInline):
    model = RelationshipSchoolClassRoom
    extra = 1


class RelationshipClassRoomStudentInline(admin.TabularInline):
    model = RelationshipClassRoomStudent
    extra = 1


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    inlines = [RelationshipSchoolClassRoomInline]


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at', 'updated_at')
    inlines = [RelationshipClassRoomStudentInline]