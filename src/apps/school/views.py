from django.db.models import Prefetch
from django.views.generic import ListView

from apps.account.models import Teacher, Student
from apps.account.mixins import AdminOrTeacherRequiredMixin

from .models import School, ClassRoom


class DashboardStudentView(AdminOrTeacherRequiredMixin, ListView):
    model = Student
    queryset = model.objects.prefetch_related(
        Prefetch('classroom', queryset=ClassRoom.objects.all())
    )
    context_object_name = 'students'
    template_name = 'dashboard/students.html'
