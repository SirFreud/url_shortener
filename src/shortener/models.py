from django.db import models


class ShortenedURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20)

    def __str__(self):
        return str(self.url)
