from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Balcony",
            "Bathroom",
            "TV",
            "Shower",
            "Sofa",
            "Stereo",
            "Towels",
            "Toilet"
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!!"))