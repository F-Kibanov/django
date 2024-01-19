import logging
from random import choice

from django.shortcuts import HttpResponse

from .models import Author, Coin, Post, Client, Product, Order

logger = logging.getLogger()


def coin(request):
    coin_state = choice(['head', 'tail'])
    logger.info(f'Function coin returns {coin_state}')
    coin_res = Coin(side=coin_state)
    coin_res.save()
    res = Coin.coin_static(3)
    return HttpResponse(f'{coin_state} ,{res}')


def authors_view(request):
    authors = Author.objects.all()
    res_str = '<br>'.join([str(author) for author in authors])
    return HttpResponse(res_str)


def post_view(request):
    posts = Post.objects.all()
    res_str = '<br>'.join([str(post) for post in posts])
    return HttpResponse(res_str)


"""Домашнее задание к семинару №2"""


def get_orders(request):
    orders = Order.objects.all()
    res_str = '<br>'.join([str(order) for order in orders])
    return HttpResponse(res_str)
