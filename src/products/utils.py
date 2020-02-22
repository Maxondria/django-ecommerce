import os
import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    Method assumes that the instance has a model with a slug field and a title character (char) field.
    """
    if new_slug:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        randstr = random_string_generator(size=4)
        new_slug = f"{slug}-{randstr}"
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 34554554)
    _name, ext = get_filename_ext(filename)
    return f"products/{new_filename}/{new_filename}{ext}"


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    return os.path.splitext(basename)
