from django.core.management.base import BaseCommand, CommandParser

from third_sem.models import Author


class Command(BaseCommand):
    help = 'Delete an author by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Author id to delete')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        author = Author.objects.filter(pk=id).first()
        self.stdout.write(self.style.ERROR(f'Deleted author: {author}'))
        author.delete()
