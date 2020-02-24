from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver

from .models import Cart


@receiver(m2m_changed, sender=Cart.products.through)
def calculate_subtotal(sender, instance, action, **kwargs):
    save_on_actions = ["post_add", "post_remove", "post_clear"]

    if action in save_on_actions:
        products = instance.products.all()
        subtotal = sum([product.price for product in products])
        if instance.subtotal != subtotal:
            instance.subtotal = subtotal
            instance.save()


@receiver(pre_save, sender=Cart)
def calculate_total(sender, instance, **kwargs):
    instance.total = instance.subtotal + 10 if instance.subtotal > 0 else 0.00
