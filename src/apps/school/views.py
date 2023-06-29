from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView

from apps.account.models import Teacher, Student
from apps.account.mixins import AdminOrTeacherRequiredMixin

from .models import School, ClassRoom, RelationshipClassRoomStudent, RelationshipSchoolClassRoom
from ..account.forms import StudentForm, StudentCreateForm


class DashboardStudentListView(AdminOrTeacherRequiredMixin, ListView):
    model = RelationshipClassRoomStudent
    queryset = model.objects.select_related('classroom', 'student')
    context_object_name = 'items'
    template_name = 'dashboard/student/list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.queryset.filter(
                Q(student__first_name__icontains=query) |
                Q(student__last_name__icontains=query)
            )
        return self.queryset


class DashboardStudentCreateView(AdminOrTeacherRequiredMixin, FormView):
    model = Student
    form_class = StudentCreateForm
    success_url = reverse_lazy('students')
    template_name = 'dashboard/student/create.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DashboardStudentDetailView(AdminOrTeacherRequiredMixin, DetailView):
    model = RelationshipClassRoomStudent
    queryset = model.objects.select_related('classroom', 'student')
    context_object_name = 'item'
    template_name = 'dashboard/student/detail.html'

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
    template_name = 'dashboard/student/update.html'

    def get_object(self, queryset=None):
        return self.get_queryset().get(id=self.kwargs.get('uuid'))


class DashboardStudentDeleteView(AdminOrTeacherRequiredMixin, DeleteView):
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy("students")
    template_name = 'dashboard/student/delete.html'

    def get_object(self, queryset=None):
        return self.get_queryset().get(id=self.kwargs.get('uuid'))
