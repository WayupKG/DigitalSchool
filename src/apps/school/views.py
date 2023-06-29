from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from apps.account.models import Teacher, Student
from apps.account.mixins import AdminOrTeacherRequiredMixin

from .models import School, ClassRoom, RelationshipClassRoomStudent, RelationshipSchoolClassRoom
from ..account.forms import StudentForm


class DashboardStudentListView(AdminOrTeacherRequiredMixin, ListView):
    model = RelationshipClassRoomStudent
    queryset = model.objects.select_related('classroom', 'student')
    context_object_name = 'items'
    template_name = 'dashboard/students.html'


class DashboardStudentDetailView(AdminOrTeacherRequiredMixin, DetailView):
    model = RelationshipClassRoomStudent
    queryset = model.objects.select_related('classroom', 'student')
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


class DashboardStudentUpdateView(AdminOrTeacherRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'dashboard/students-update.html'

    def get_object(self, queryset=None):
        return self.get_queryset().get(id=self.kwargs.get('uuid'))


class DashboardStudentDeleteView(AdminOrTeacherRequiredMixin, DeleteView):
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy("students")
    template_name = 'dashboard/students-delete.html'

    def get_object(self, queryset=None):
        return self.get_queryset().get(id=self.kwargs.get('uuid'))
