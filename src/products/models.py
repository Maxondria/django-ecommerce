import os
import random

from django.db import models
from django.shortcuts import get_object_or_404
from .utils import upload_image_path, unique_slug_generator
from django.urls import reverse
from PIL import Image


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        """featured() is added on the real queryset, so it supports chaining!"""
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # overwrite all() on queryset
    def all(self):
        return self.get_queryset().active()

    def find_by_slug(self, slug):
        return self.get_queryset().filter(slug=slug, active=True)

    def features(self):
        return self.get_queryset().featured()


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.title}"
