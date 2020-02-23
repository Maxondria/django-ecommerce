from django.urls import path

from .views import (
    ProductDetailView,
    ProductFeaturedDetailView,
    ProductFeaturedListView,
    ProductListView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("all/featured/", ProductFeaturedListView.as_view(), name="featured-list"),
    path(
        "featured/<slug:slug>/",
        ProductFeaturedDetailView.as_view(),
        name="featured-detail",
    ),
]

app_name = "products"
