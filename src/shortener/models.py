from django.conf import settings
from django.db import models
from .utils import code_generator, create_shortcode

# Goes through the settings file and searches for the variable named 'SHORTCODE_MAX', if not found, sets variable to 20
SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 20)

class ShortenedURLManager(models.Manager):

    def all(self, *args, **kwargs):
        # This is the default behavior of the save function
        qs_main = super(ShortenedURLManager, self).all(*args, **kwargs)
        # This allows to filter out all inactive URLs from being returned with the all() method
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = ShortenedURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made {i}".format(i=new_codes)


class ShortenedURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)  # auto_now means that every time the model is saved - it's going to set that time value
    timestamp = models.DateTimeField(auto_now_add=True)  # sets time value when first created
    active = models.BooleanField(default=True)
    # This changes the original Model Manager to the ShortenedURL Manager I created above!
    objects = ShortenedURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortenedURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
