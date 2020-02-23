from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Tag
from products.utils import unique_slug_generator


@receiver(pre_save, sender=Tag)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
