#### Configure Statics

- Create static_cdn directory on the root directory, the same directory as `src` as this will act as a real CDN for development
- Head to project settings files and add this configuration:

* Please note that `BASE_DIR` is the folder where the `manage.py` and main project reside. In our case, the `src` directory.

* Also, create a folder `local_static` in `src` for the Django app to sort of handle static files during dev.

```python 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "local_static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")
```
- Head to the main `urls.py` file and configure the dev environment static files like:

```python 
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
- Run the following command to collect all the static files to `static_cdn` directory:
```python manage.py collectstatic```

This will collect and like CDN compile our files and copy them to `static_cdn/static_root/ ` and any picture uploads or other media to `static_cdn/media_root/`:

And all we can do now is create our static directories like `css` directory in `src/local_static/` and running the command above does the work of making copies into the CDN directory