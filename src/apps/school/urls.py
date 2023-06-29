from django.urls import path, include

from .import views

students_urlpatterns = [
    path('', views.DashboardStudentListView.as_view(), name='students'),
]

urlpatterns = (
    path('students/', include(students_urlpatterns)),
)
