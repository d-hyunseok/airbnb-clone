from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--number", default=50, type=int, help="")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!!"))