from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Product
from ecommerce.utils import unique_slug_generator


@receiver(pre_save, sender=Product)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
