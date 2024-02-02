import datetime
from django.db import models


class Coin(models.Model):
    side = models.CharField(max_length=5)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Coin side is {self.side} in {self.time_created}'

    @staticmethod
    def coin_static(count):
        coin_static = Coin.objects.all()[:count]
        coin_dict = {
            'head': [],
            'tail': []
        }
        for coin in coin_static:
            if coin.side == 'head':
                coin_dict['head'].append(coin.time_created)
            elif coin.side == 'tail':
                coin_dict['tail'].append(coin.time_created)
            else:
                print('Coin error!!')
        return coin_dict


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'Author: {self.name} {self.surname}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}'


"""Домашнее задание к семинару №2"""


class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.name} {self.surname}, email: {self.email}, ' \
               f'phone: {self.phone}, address: {self.address}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.IntegerField(default=0)
    product_add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.product_name}, product description: {self.product_description}, ' \
               f'product price: {self.product_price}, product quantity: {self.product_quantity}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client {self.client} ordered {self.product} at total price {self.total_price}'
