from django.shortcuts import render, Http404
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    # Option A: overwrite ->: queryset = Product.find_all(),
    # model = Product, is shorthand for saying: queryset = Product.objects.all()

    # Option B: overwrite the 'get_queryset()' method and return as you please
    # def get_queryset(self):
    #     # queryset = super().get_queryset()
    #     return Product.objects.all()

    # https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/

    model = Product
    context_object_name = "products"

    # def get_context_data(self, **kwargs): -> This is what is displayed in the template
    #     context = super().get_context_data(**kwargs)
    #     context['something'] = 123
    #     return context


class ProductDetailView(DetailView):
    context_object_name = "product"
    # model = Product

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Product.objects.find_by_slug(slug=slug)


class ProductFeaturedListView(ListView):
    template_name = "products/featured_list.html"
    context_object_name = "products"
    queryset = Product.objects.features()


class ProductFeaturedDetailView(DetailView):
    context_object_name = "product"
    template_name = "products/featured_detail.html"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Product.objects.features().filter(slug=slug, active=True)
