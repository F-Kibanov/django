from django.core.management.base import BaseCommand, CommandParser

from third_sem.models import Client, Product, Order


"""Домашнее задание к семинару №3"""


class Command(BaseCommand):
    help = 'Create a test order to fill database'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('Client ID', type=int, help='ID of the client to make an order')
        parser.add_argument('Product ID', type=int, help='ID of the product to make an order')
        parser.add_argument('Product quantity', type=int, help='Quantity of the product')

    def handle(self, *args, **kwargs):
        client_id = kwargs['Client ID']
        product_id = kwargs['Product ID']
        product_quantity = kwargs['Product quantity']
        order = Order(
            client=Client.objects.get(id=client_id),
            product=Product.objects.get(id=product_id),
            total_price=int(product_quantity)*int(Product.objects.get(id=product_id).product_price)
        )
        self.stdout.write(self.style.SUCCESS(f'Created order: {order}'))
        order.save()
