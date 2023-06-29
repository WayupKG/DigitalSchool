from django.urls import path, include

from .import views

students_urlpatterns = [
    path('/', views.DashboardStudentView.as_view(), name='students'),
]

urlpatterns = (
    path('students/', include(students_urlpatterns)),
)
