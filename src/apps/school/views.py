from django.db.models import Prefetch
from django.views.generic import ListView

from apps.account.models import Teacher, Student
from apps.account.mixins import AdminOrTeacherRequiredMixin

from .models import School, ClassRoom, RelationshipClassRoomStudent, RelationshipSchoolClassRoom


class DashboardStudentListView(AdminOrTeacherRequiredMixin, ListView):
    model = RelationshipClassRoomStudent
    queryset = model.objects.select_related('classroom', 'student')
    context_object_name = 'items'
    template_name = 'dashboard/students.html'
