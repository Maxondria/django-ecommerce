from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = "search/view.html"
    context_object_name = "products"

    def get_queryset(self):
        request = self.request
        q = request.GET.get("q", None)
        return (
            Product.objects.filter(title__icontains=q)
            if q
            else Product.objects.features()
        )

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context
