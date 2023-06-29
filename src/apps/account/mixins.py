from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

from common import constants as const


class IsNotAuthenticatedMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(IsNotAuthenticatedMixin, self).dispatch(request, *args, **kwargs)


class AdminOrTeacherRequiredMixin(AccessMixin):
    """Убедитесь, что текущий пользователь является Учителем."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.user_type in [const.ADMIN, const.TEACHER]:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)