import datetime
from typing import Any
from django.core.management.base import BaseCommand

from second_sem.models import Author


class Command(BaseCommand):
    help = 'Creates new users'

    def handle(self, *args, **options):
        for i in range(1, 11):
            author = Author(name=f'Name{i}',
                            surname=f'Surname{i}',
                            email=f'email{i}@test.com',
                            bio=f'Bio{i}',
                            birthday=datetime.date(2000, 1, 1)
                            )
            self.stdout.write(self.style.ERROR(f'Author {author} created'))
            author.save()

