from django.views.generic import ListView, DetailView

from apps.account.models import Teacher, Student
from apps.account.mixins import AdminOrTeacherRequiredMixin

from .models import School, ClassRoom, RelationshipClassRoomStudent, RelationshipSchoolClassRoom


class DashboardStudentListView(AdminOrTeacherRequiredMixin, ListView):
    model = RelationshipClassRoomStudent
    queryset = model.objects.select_related('classroom', 'student')
    context_object_name = 'items'
    template_name = 'dashboard/students.html'


class DashboardStudentDetailView(AdminOrTeacherRequiredMixin, DetailView):
    model = RelationshipClassRoomStudent
    context_object_name = 'item'
    template_name = 'dashboard/students-detail.html'

    def get_object(self, queryset=None):
        return self.get_queryset().get(student__id=self.kwargs.get('uuid'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = RelationshipSchoolClassRoom.objects.select_related(
            'school'
        ).get(
            classroom=self.get_object().classroom
        )
        return context
