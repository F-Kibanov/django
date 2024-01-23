from django.core.management.base import BaseCommand
from third_sem.models import Client


"""Домашнее задание к семинару №2"""


class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            client = Client(
                name=f'Name{i}',
                surname=f'Surname{i}',
                email=f'Email{i}@test.com',
                phone=f'Phone{i}',
                address=f'Address{i}'
            )
            self.stdout.write(self.style.ERROR(f'Client {client} created'))
            client.save()
