from django.urls import path, include

from . import views

urlpatterns = [
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
