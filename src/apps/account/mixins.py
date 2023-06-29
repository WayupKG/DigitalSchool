from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class IsNotAuthenticatedMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(IsNotAuthenticatedMixin, self).dispatch(request, *args, **kwargs)
