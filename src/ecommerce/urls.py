from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import about_page, contact_page, home_page, login_page, register_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home"),
    path("contact/", contact_page, name="contact"),
    path("about/", about_page, name="about"),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("products/", include("products.urls", namespace="products")),
    path("search/", include("search.urls", namespace="search")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
