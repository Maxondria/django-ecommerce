from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import login_page, register_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
