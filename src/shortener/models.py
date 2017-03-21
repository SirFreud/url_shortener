from django.db import models


class ShortenedURL(models.Model):
    url       = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20, unique=True)
    update    = models.DateTimeField(auto_now=True)  # auto_now means that every time the model is saved - it's going to set that time value
    timestamp = models.DateTimeField(auto_now_add=True)  # sets time value when first created

    def __str__(self):
        return str(self.url)
