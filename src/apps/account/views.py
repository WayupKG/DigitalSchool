from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View, TemplateView, DetailView, FormView, ListView, CreateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model, password_validation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from .mixins import IsNotAuthenticatedMixin
from .forms import AuthenticationForm


class SignInView(IsNotAuthenticatedMixin, FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'auth/sign-in.html'

    def form_valid(self, form):
        redirect_to = self.request.GET.get('next', None)
        login(self.request, form.get_user())
        if redirect_to:
            return redirect(redirect_to)
        return super().form_valid(form)


class LogoutView(View):
    """Выход"""
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('sign_in')
