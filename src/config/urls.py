from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', RedirectView.as_view(pattern_name='sign_in', permanent=True)),
    path('', RedirectView.as_view(pattern_name='students', permanent=True)),
    path('accounts/', include('apps.account.urls')),
    path('dashboard/', include('apps.school.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)),)
