from django.db import models
from .utils import code_generator, create_shortcode


class ShortenedURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)  # auto_now means that every time the model is saved - it's going to set that time value
    timestamp = models.DateTimeField(auto_now_add=True)  # sets time value when first created

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortenedURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
