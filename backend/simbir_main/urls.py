from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

handler404 = "notes.views.page_not_found"
handler500 = "notes.views.server_error"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("allauth.urls")),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("notes.urls", namespace='note')),
    path("api/", include("api.urls", namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
