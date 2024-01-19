from django.core.management.base import BaseCommand
from second_sem.models import Product


"""Домашнее задание к семинару №2"""


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            product = Product(
                product_name=f'Product{i}',
                product_description=f'Product description{i}',
                product_price=i,
                product_quantity=i,
            )
            self.stdout.write(self.style.ERROR(f'Product {product} created'))
            product.save()
