from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortenedURL

class Command(BaseCommand):
    help = 'Refreshes all ShortenedURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        parser.add_argument('number3', type=int)

    def handle(self, *args, **options):
        print(options)
        ShortenedURL.objects.refresh_shortcodes()
