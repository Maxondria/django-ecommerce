from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        user = request.user if request.user.is_authenticated else None

        qs = self.get_queryset().filter(id=cart_id)
        if qs.exists():
            is_new_cart = False
            cart = qs.first()
            if user and not cart.user:
                cart.user = user
                cart.save()
        else:
            cart = self.new(user=user)
            request.session["cart_id"] = cart.id
            is_new_cart = True
        return cart, is_new_cart

    def new(self, user=None):
        return self.model.objects.create(user=user)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)
