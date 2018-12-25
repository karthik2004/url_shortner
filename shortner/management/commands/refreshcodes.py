from django.core.management.base import BaseCommand,CommandError
from shortner.models import shortnerURL

class Command(BaseCommand):
    help = 'refreshes all codes'


    def handle(self, *args, **options):
        return shortnerURL.objects.refresh_shortcodes()