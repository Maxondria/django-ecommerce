from django.db import models

from carts.models import Cart

ORDER_STATUS_CHOICES = (
    ("created", "Created"),
    ("paid", "Paid"),
    ("shipped", "Shipped"),
    ("refunded", "Refunded"),
)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(
        default="created", max_length=50, choices=ORDER_STATUS_CHOICES
    )
    order_id = models.CharField(max_length=120, blank=True)
    shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def update_total(self):
        self.total = self.cart.total + self.shipping_total
        self.save()

    def __str__(self):
        return self.order_id
