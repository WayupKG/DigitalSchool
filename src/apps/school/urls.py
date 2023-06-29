from django.urls import path, include

from .import views

students_urlpatterns = [
    path('', views.DashboardStudentListView.as_view(), name='students'),
    path('create/', views.DashboardStudentCreateView.as_view(), name='students_create'),
    path('detail/<str:uuid>/', views.DashboardStudentDetailView.as_view(), name='students_detail'),
    path('update/<str:uuid>/', views.DashboardStudentUpdateView.as_view(), name='students_update'),
    path('delete/<str:uuid>/', views.DashboardStudentDeleteView.as_view(), name='students_delete'),
]

urlpatterns = (
    path('students/', include(students_urlpatterns)),
)
