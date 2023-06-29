from django.urls import path, include

from .import views

students_urlpatterns = [
    path('', views.DashboardStudentListView.as_view(), name='students'),
    path('detail/<str:uuid>/', views.DashboardStudentDetailView.as_view(), name='students_detail'),
]

urlpatterns = (
    path('students/', include(students_urlpatterns)),
)
