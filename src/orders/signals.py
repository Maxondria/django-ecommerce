from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from ecommerce.utils import unique_id_generator

from .models import Order
from carts.models import Cart


@receiver(pre_save, sender=Order)
def create_order_id(sender, instance, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_id_generator(instance)


@receiver(post_save, sender=Cart)
def cart_post_save(sender, instance, created, **kwargs):
    """ Update order cart total, takes effect only on updating cart """
    if not created:
        cart_id = instance.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order = qs.first()
            order.update_total()


@receiver(post_save, sender=Order)
def order_post_save(sender, instance, created, **kwargs):
    """ After saving a new order, takes effect on creating an order """
    if created:
        instance.update_total()
