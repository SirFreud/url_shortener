import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for i in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    # This line is the same as the four lines above, just condensed
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    # This gets the class directly from the instance varible. Kind of like importing the class without actually doing the import
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    ShortenedURL = instance.__class__
    qs_exists = ShortenedURL.objects.filter(shortcode=new_code).exists()
    # Recursively checking for duplicates in shortcodes
    # If the shortcode created already exists in the database, we run the function again to create another shortcode
    # If queryset doesn't already exist in the DB (False), then it's unqieu so we can return
    if qs_exists:
        return create_shortcode(size=size)

    return new_code
